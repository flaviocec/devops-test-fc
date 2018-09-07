# devops-test

Kurt Geiger DevOps test

KGDevOpsInterview.json is a CF template that will spin up an EC2 instance. Tasks:

1) fix the errors in the template
2) tag the EC2 instance with with the key 'Name' and the value your first and last name
3) modify the stack so that yum update is executed when the instances comes up
4) output the EC2 instance ID

test.rb is a simple Chef recipe that installs Apache and writes 'Hello world' in /etc/motd. Tasks:

1) fix the syntax/errors in the recipe
2) set httpd to be enabled at boot time
3) create a *nix username called your firstname.lastname using the 'user' Chef resource
