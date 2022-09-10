# tekever_challenge

Swagger API [link](https://app.swaggerhub.com/apis/ffriande/tekever_challenge/1.0.0)


## Running server instructions:

1. Make sure to have Docker daemon up and running

3. Build docker image locally

```
docker build -t tekever_api .
```

3. Run container

```
docker run -p 5001:5000 -it tekever_api
```

4. Test!

For testing **create_account**,
```
curl -X POST -H "Content-type: application/json" -d "{\"customerID\" : \"1\", \"initialCredit\" : \"3\"}" "localhost:5001/create_account"
```

For testing **user_info**,
```
curl "localhost:5001/user_info?customerID=1"
```

And play with the arguments.

Note: Endpoint GET named "dump_db" also exists for debug purposes, curling to it will reveal all db data.

