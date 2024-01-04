# AWS
```bash
cz bump -ch
python3 -m build

export CODEARTIFACT_AUTH_TOKEN=`aws codeartifact get-authorization-token --domain $DOMAIN --domain-owner $OWNER --region $AWS_REGION --query authorizationToken --output text`

export TWINE_USERNAME=aws
export TWINE_PASSWORD=$CODEARTIFACT_AUTH_TOKEN
export TWINE_REPOSITORY_URL=<PUT YOUR REPOSITORY URL>

python3 -m twine upload dist/*$(cz version -p)*
```
