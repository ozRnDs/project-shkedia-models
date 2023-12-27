- [Overview](#overview)
- [Models](#models)


# Overview

The project manages diverse data. This module is design to keep all the services updated with the same data structures (from now on would be referred as models).  
Most of the data is stored in relational db (Postgresql) and the models will include important interface to basic sql commands (Create Table, Selects, etc).  
All the models will be based on pydantic's BaseModel class. The class handles easy integration with FastAPI and json structured messages.

# Models
Each model represent an object in our system. The user or the system can interact with that object. These our objects:
1. User - Describes the user. Used for authentication and data owning process.
2. Device - Describes the device. Could be also referred as media's source.
3. Media - Describes the media's basic information (Owners - User and Device, Date, Thumbnail, etc)
4. InsightEngine - Describes the types of filter/properties/information we can extract from image. These are the system filters (by date, by object, by face, etc)
5. Insight (Property) - Describes specific Property found in a specific image
6. InsightJob - Describes the images that were analyzed using insight engines
7. Collection - Describes collections of media
