import logging
logger = logging.getLogger(__name__)
from typing import TypeVar
from pydantic import BaseModel

class SqlEngine():

    def __init__(self, environment: str="dev") -> None:
        self.environment = environment

    @staticmethod
    def __sql_create_table__():
        raise NotImplementedError()

    def __sql_insert__(self, object_to_insert: BaseModel):
        columns = []
        values = []
        for field_name, field_value in object_to_insert.model_dump().items():
            if field_value:
                columns.append(field_name)
                values.append(field_value)

        sql_template = "INSERT INTO "+ self.get_table_name_from_object(object_to_insert) + " (" + ",".join(columns) + ") VALUES ("+",".join(["%s"]*len(columns))+")"
        values = (tuple)(values)
        return sql_template, values
    
    def __sql_select_item__(self, object: BaseModel, field_names, field_values):
        sql_template = f"SELECT * FROM "+self.get_table_name_from_object(object)+" WHERE"
        search_string = []
        sql_values=[]
        for field_index, field_name in enumerate(field_names):
            if not field_name in object.model_dump():
                raise KeyError(f"Field {field_name} doesn't exists in the object")
            field_search = f"{field_name} IN (" + ",".join(["%s"]*len(field_values[field_index])) + ")"
            search_string.append(field_search)
            sql_values+=field_values[field_index]
        sql_template += " "+" AND ".join(search_string)
        return sql_template, (tuple)(sql_values)

    def __sql_update_item__(self, object, update_dictionary):
        values = []
        update_list = []
        sql_template = f"UPDATE "+ self.get_table_name_from_object(object) +" SET "
        for field_name, field_value in update_dictionary.items():
            if not field_value:
                update_list.append(f"{field_name}=''")
                continue
            update_list.append(f"{field_name}=%s")
            values.append(field_value)
        sql_template += ",".join(update_list)
        sql_template += " WHERE id=%s"
        values.append(object.id)

        values = (tuple)(values)
        return sql_template, values

    def __sql_delete_item__(self, environment: str):
        raise NotImplementedError()

    def __does_table_exists__(self):
        raise NotImplementedError("I still don't know that. In the near future")
        table_name = get_table_name_from_object(self)
        sql_template = ...
        return ...

    def __get_updated_values__(self: BaseModel, updated_model: BaseModel):
        current_dictionary = self.model_dump()
        new_dictionary = updated_model.model_dump()
        # Make sure the item's id can't change - extract it from update_model
        id_field_name = type(self).__name__.lower().replace("db","") + "_id"
        new_dictionary.pop(id_field_name)
        current_dictionary.pop(id_field_name)

        update_dictionary = {}
        for field_name, field_value in current_dictionary.items():
            if not field_name in new_dictionary:
                update_dictionary[field_name]=new_dictionary[field_name]
                continue
            if field_value != new_dictionary[field_name]:
                update_dictionary[field_name]=new_dictionary[field_name]
        return update_dictionary

    def get_table_name_from_object(self, object: BaseModel):
        return object.__class__.__name__.lower()+"s_"+self.environment

TSqlModel = TypeVar("TSqlModel", bound=SqlEngine)