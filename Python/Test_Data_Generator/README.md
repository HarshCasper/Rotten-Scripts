# Test_Data_Generator

## Dependencies

- Faker

Faker is a Python package that generates fake data.

Syntax
```py
faker.Faker()
```
Creates and initializes a faker generator, which can generate data by accessing properties named after the type of data we want.
Each call to method fake.name() yields a different (random) result. This is because faker forwards faker.Generator.method_name() calls to faker.Generator.format(method_name).

## Working of Code

This code asks the user's input for the numbers of entries required and generates a fake test dataset comprising of student details enrolled in online courses.

The parameters of the constructed dataset are-

1. Student ID

2. Student Name

3. Email Id

4. Phone Number

5. Date of Birth

6. House Address

7. Latitude

8. Longitude

9. Country

10. Course Comments

## Saving/Exporting Dataset

The generated dataset consisting of the specified number of entries from the user is then exported to the local device in `csv` format.
