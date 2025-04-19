# lith

**lith** is a template for a Django application deployed using Terraform in a highly-available and scalable AWS environment.

## Local Development

Docker, Docker Compose, and Make are required for this project.

```console
$ make up # starts a local server
```

Refer to the [Makefile](./Makefile) for all the available commands.

## Deployment

```console
$ make bootstrap          # creates the Terraform storage and lock table in AWS
$ make deploy             # creates the main Terraform resources
$ make undeploy           # destroys ALL resources
$ make tf-partial-destroy # destroys the main Terraform resources but keeps the bootstrap resources
```

It might be a good idea to run `make tf-partial-destroy` after merging to master if we want to keep costs down.
