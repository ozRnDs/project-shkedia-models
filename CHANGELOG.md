## 0.6.0 (2024-01-05)

### Feat

- **insights**: Add prob field to InsightBasic

## 0.5.0 (2024-01-04)

### Feat

- **SearchResult**: Add property number_of_pages

### Fix

- **media**: Change MediaThumbnail to inherate from both MediaDevice and MediaMetadata

## 0.4.4 (2024-01-04)

### Fix

- **collection.CollectionPreview**: Add media_key to decrypt the thumbnail

## 0.4.3 (2024-01-04)

### Fix

- **device**: Fix typo in field_serializer field name

## 0.4.2 (2024-01-04)

### Fix

- **insights**: Change InsightEngineValues field name from insights to insights_names

## 0.4.1 (2024-01-04)

### Fix

- **insights**: Set default for InsightEngineValues.insights = []

## 0.4.0 (2024-01-04)

### Feat

- **insights**: Add InsightEngineValues object

## 0.3.3 (2024-01-04)

### Fix

- **jobs,media**: Serialize InsightJob.net_time_seconds, MediaRequest.create_on

### Refactor

- **insights**: Delete duplicate definition for InsightEngine

## 0.3.2 (2024-01-04)

### Fix

- **device,media,user,token**: Rename token.py to auth.py. Add to all the timedate fields serializer to str

## 0.3.1 (2024-01-01)

### Fix

- **jobs**: Fix start_time default lambda. Add field_serializer to return isoformat

## 0.3.0 (2023-12-31)

### Feat

- **insights**: Add job_id to InsightBasic

## 0.2.0 (2023-12-28)

### Feat

- **jobs**: Adding jobs related models

### Refactor

- **media/MediaIDs**: Move upload_status field to MediaIDs from the MediaDevice

## 0.1.0 (2023-12-27)

### Feat

- **package**: Create the package basics

### Fix

- **token**: Add missing model for token
- **search**: Add missing search model

### Refactor

- **models**: Create SqlAlchemy version to the models
