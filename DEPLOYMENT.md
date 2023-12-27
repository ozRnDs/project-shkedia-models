# AWS
```bash
export TWINE_USERNAME=aws
export TWINE_PASSWORD=`aws codeartifact get-authorization-token --domain my_domain --domain-owner 111122223333 --query authorizationToken --output text`
export TWINE_REPOSITORY_URL=`aws codeartifact get-repository-endpoint --domain my_domain --domain-owner 111122223333 --repository my_repo --format pypi --query repositoryEndpoint --output text`
```
