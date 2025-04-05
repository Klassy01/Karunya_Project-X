from flask import Flask, request, jsonify
from flask_cors import CORS
import random


app = Flask(__name__)
CORS(app)

# MCQs for Java and Python
questions_data = {
    "Java": {
        "Beginner": [
            {"text": "What is Java?", "options": ["Programming Language", "Database", "Operating System", "Text Editor"], "correct": "Programming Language"},
            {"text": "Which keyword is used to define a class in Java?", "options": ["define", "class", "struct", "object"], "correct": "class"},
            {"text": "What is JVM?", "options": ["Java Virtual Machine", "Java Variable Memory", "Java Verification Mode", "None of these"], "correct": "Java Virtual Machine"},
            {"text": "Which data type is used to store decimal values?", "options": ["int", "boolean", "double", "char"], "correct": "double"},
            {"text": "Which symbol is used for single-line comments in Java?", "options": ["//", "/*", "#", "--"], "correct": "//"},
            {"text": "Which operator is used to compare two values in Java?", "options": ["=", "==", "!=", "<>"], "correct": "=="},
            {"text": "Which keyword is used to create an object in Java?", "options": ["new", "object", "create", "instance"], "correct": "new"},
            {"text": "What is the default value of an int variable in Java?", "options": ["0", "null", "undefined", "-1"], "correct": "0"},
            {"text": "Which loop is used for a fixed number of iterations?", "options": ["while", "do-while", "for", "switch"], "correct": "for"},
            {"text": "Which Java feature allows code reuse?", "options": ["Encapsulation", "Polymorphism", "Inheritance", "Abstraction"], "correct": "Inheritance"},
        ],
        "Intermediate": [
            {"text": "Which keyword is used for exception handling in Java?", "options": ["catch", "throw", "try", "All of the above"], "correct": "All of the above"},
            {"text": "Which Java feature restricts access to methods and variables?", "options": ["Encapsulation", "Inheritance", "Polymorphism", "Abstraction"], "correct": "Encapsulation"},
            {"text": "Which Java collection is synchronized?", "options": ["ArrayList", "HashSet", "Vector", "TreeMap"], "correct": "Vector"},
            {"text": "What does the `static` keyword do in Java?", "options": ["Creates an instance variable", "Allocates memory dynamically", "Makes a variable/method belong to the class", "None of these"], "correct": "Makes a variable/method belong to the class"},
            {"text": "Which method is used to read a line of text in Java?", "options": ["nextLine()", "readLine()", "getLine()", "inputLine()"], "correct": "readLine()"},
            {"text": "Which Java keyword is used to prevent method overriding?", "options": ["static", "final", "const", "private"], "correct": "final"},
            {"text": "Which interface is used for JDBC connection?", "options": ["Connection", "Statement", "ResultSet", "Database"], "correct": "Connection"},
            {"text": "Which data structure follows LIFO?", "options": ["Queue", "Stack", "Array", "LinkedList"], "correct": "Stack"},
            {"text": "Which class is the parent of all Java classes?", "options": ["Object", "Parent", "Base", "Super"], "correct": "Object"},
            {"text": "What is the default capacity of an `ArrayList`?", "options": ["5", "10", "15", "20"], "correct": "10"},
        ],
        "Advanced": [
            {"text": "What is polymorphism in Java?", "options": ["Multiple forms", "Single form", "Data hiding", "None"], "correct": "Multiple forms"},
            {"text": "Which collection type maintains insertion order?", "options": ["HashSet", "TreeSet", "ArrayList", "HashMap"], "correct": "ArrayList"},
            {"text": "What is multithreading?", "options": ["Executing multiple tasks simultaneously", "Running a single thread", "Executing Java code in parallel", "None"], "correct": "Executing multiple tasks simultaneously"},
            {"text": "Which Java framework is used for web development?", "options": ["Spring", "React", "Angular", "Django"], "correct": "Spring"},
            {"text": "Which method starts a thread in Java?", "options": ["run()", "start()", "execute()", "begin()"], "correct": "start()"},
            {"text": "Which Java class is used for reading a file?", "options": ["FileReader", "BufferedReader", "Scanner", "All of the above"], "correct": "All of the above"},
            {"text": "What is the purpose of garbage collection in Java?", "options": ["Memory management", "Security", "Performance optimization", "None of the above"], "correct": "Memory management"},
            {"text": "Which design pattern is used for object creation?", "options": ["Singleton", "Observer", "Factory", "Builder"], "correct": "Factory"},
            {"text": "What is the use of the volatile keyword in Java?", "options": ["Thread synchronization", "Memory management", "Data hiding", "None of these"], "correct": "Thread synchronization"},
            {"text": "Which package contains collection framework classes?", "options": ["java.util", "java.io", "java.sql", "java.net"], "correct": "java.util"},
        ],
    },
    "Python": {
        "Beginner": [
            {"text": "What is Python?", "options": ["Programming language", "Snake", "IDE", "Database"], "correct": "Programming language"},
            {"text": "Which library is used for data analysis?", "options": ["NumPy", "Pandas", "Scikit-learn", "Matplotlib"], "correct": "Pandas"},
            {"text": "Which symbol is used for comments in Python?", "options": ["//", "/*", "#", "--"], "correct": "#"},
            {"text": "Which keyword is used to define a function?", "options": ["def", "func", "define", "function"], "correct": "def"},
            {"text": "Which data type is mutable?", "options": ["Tuple", "List", "String", "Integer"], "correct": "List"},
            {"text": "Which operator is used for exponentiation?", "options": ["^", "**", "*", "//"], "correct": "**"},
            {"text": "Which Python module is used for working with JSON?", "options": ["json", "pickle", "csv", "os"], "correct": "json"},
            {"text": "What is the output of print(3 * 'Python')?", "options": ["Python3", "PythonPythonPython", "Error", "Python*3"], "correct": "PythonPythonPython"},
            {"text": "How do you create a list in Python?", "options": ["[]", "{}", "()", "||"], "correct": "[]"},
            {"text": "What is the default return value of a function that doesn't return anything?", "options": ["None", "0", "Empty String", "False"], "correct": "None"},
        ],
        "Intermediate": [
    {"text": "Which method is used to remove whitespace from a string?", 
     "options": ["strip()", "remove()", "delete()", "clean()"], "correct": "strip()"},
    
    {"text": "Which of the following is a mutable data type in Python?", 
     "options": ["Tuple", "List", "String", "Integer"], "correct": "List"},
    
    {"text": "What will list(range(5, 0, -1)) return?", 
     "options": ["[1, 2, 3, 4, 5]", "[5, 4, 3, 2, 1]", "[0, 1, 2, 3, 4]", "None"], "correct": "[5, 4, 3, 2, 1]"},
    
    {"text": "Which Python function is used to open a file?", 
     "options": ["open()", "read()", "write()", "file()"], "correct": "open()"},
    
    {"text": "Which keyword is used to define an anonymous function in Python?", 
     "options": ["def", "lambda", "func", "anon"], "correct": "lambda"},
    
    {"text": "Which module is used for handling JSON data?", 
     "options": ["json", "pickle", "csv", "os"], "correct": "json"},
    
    {"text": "Which operator is used for exponentiation in Python?", 
     "options": ["^", "**", "*", "//"], "correct": "**"},
    
    {"text": "Which Python library is commonly used for data analysis?", 
     "options": ["NumPy", "Pandas", "Scikit-learn", "Matplotlib"], "correct": "Pandas"},
    
    {"text": "What is the purpose of the 'with' statement in Python?", 
     "options": ["Looping", "Exception handling", "Resource management", "Error handling"], "correct": "Resource management"},
    
    {"text": "Which function is used to get user input in Python?", 
     "options": ["input()", "get()", "read()", "scan()"], "correct": "input()"}
],

"Advanced": [
    {"text": "What is a Python decorator?", 
     "options": ["Function modifier", "Class name", "Variable type", "Loop control"], "correct": "Function modifier"},
    
    {"text": "What is the difference between deep copy and shallow copy?", 
     "options": ["No difference", "Deep copy copies references", "Shallow copy copies objects", "Deep copy creates independent objects"], "correct": "Deep copy creates independent objects"},
    
    {"text": "Which Python library is used for deep learning?", 
     "options": ["PyTorch", "Django", "Flask", "Selenium"], "correct": "PyTorch"},
    
    {"text": "Which built-in function returns an iterator in Python?", 
     "options": ["iter()", "next()", "range()", "all()"], "correct": "iter()"},
    
    {"text": "What is the default mode of the open() function in Python?", 
     "options": ["r", "w", "a", "rw"], "correct": "r"},
    
    {"text": "Which module is used for regular expressions in Python?", 
     "options": ["regex", "re", "pattern", "match"], "correct": "re"},
    
    {"text": "Which method is used to join elements of a list into a string?", 
     "options": ["concat()", "append()", "join()", "merge()"], "correct": "join()"},
    
    {"text": "Which Python module is used for handling HTTP requests?", 
     "options": ["requests", "http", "urllib", "socket"], "correct": "requests"},
    
    {"text": "Which keyword is used to define a generator function in Python?", 
     "options": ["yield", "return", "generate", "async"], "correct": "yield"},
    
    {"text": "Which Python function is used to serialize an object into a string?", 
     "options": ["pickle.dump()", "json.dumps()", "serialize()", "store()"], "correct": "json.dumps()"}
]

    }
}

@app.route('/generate-mcq', methods=['POST'])
def generate_mcq():
    data = request.json
    course = data.get("course", "Java")
    
    if course not in questions_data:
        return jsonify({"error": "Invalid course"}), 400
    
    selected_questions = []
    
    # Fetching a balanced set of questions
    for level, count in zip(["Beginner", "Intermediate", "Advanced"], [4, 3, 3]):
        level_questions = questions_data[course].get(level, [])
        selected_questions.extend(random.sample(level_questions, min(count, len(level_questions))))
    
    random.shuffle(selected_questions)  # Shuffle to mix difficulty levels
    
    return jsonify({"questions": selected_questions})

if __name__ == '__main__':
    app.run(port=5001, debug=True)
