# README

## Library used for the generation of fake data

### Faker

Faker is a Python package that generates fake data.

#### Syntax

faker.Faker() - Creates and initializes a faker generator, which can generate data by accessing properties named after the type of data we want.
Each call to method fake.name() yields a different (random) result. This is because faker forwards faker.Generator.method_name() calls to faker.Generator.format(method_name).

## Working of Code

This code asks the user's input for the numbers of entries required and generates a fake test dataset comprising of student details enrolled in online courses.

The parameters of the constructed dataset are-

Student ID

Student Name

Email Id

Phone Number

Date of Birth

House Address

Latitude

Longitude

Country

Course Comments

## Saving/Exporting Dataset

The generated dataset consisting of the specified number of entries from the user is then exported to the local device in csv format.


```python

```
