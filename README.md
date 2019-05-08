# question_parser
##### CISC 4900 group project

##### Test Q&A data for CIS department undergrad program:
```yaml
---
- q: Where is the CIS department?
  a: It's in room 2109 Ingersoll Hall
- q: What majors can I choose from?
  a: B.S. in Computer Science (Java), B.S. in Multimedia Computing (Java), and B.S. in Information Systems (Java)
- q: Where can I find all the available courses?
  a: Check out this link http://www.brooklyn.cuny.edu/web/academics/schools/naturalsciences/departments/computers/graduate/courses_g.php?sch=n&div=G&disc=CISC.&department=22&dept_id=109
```

### setup
Python 3.6.8
64bit

### rasa
```sh
pip install -U rasa_core
pip install rasa_nlu[tensorflow]
python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose
python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue

```

### Trouble shooting
on windows, run the following to set up build tools first if you run into any compile errors when installing any of the above dependencies
```cmd
%comspec% /k "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall.bat" amd64 8.1
```
also make sure you're using latest python or else you might get error related to the typing package

### How can I contribute?
```ruby
"R29ldHo0OTAwOzQ5MDBDaGF0Qm90\n"
```