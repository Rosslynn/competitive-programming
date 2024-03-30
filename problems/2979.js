/*
Given a string str, return parsed JSON parsedStr. You may assume the str is a valid JSON string hence it only includes strings, numbers, arrays, objects, booleans, and null. str will not include invisible characters and escape characters. 

Please solve it without using the built-in JSON.parse method.

 

Example 1:

Input: str = '{"a":2,"b":[1,2,3]}'
Output: {"a":2,"b":[1,2,3]}
Explanation: Returns the object represented by the JSON string.
Example 2:

Input: str = 'true'
Output: true
Explanation: Primitive types are valid JSON.
Example 3:

Input: str = '[1,5,"false",{"a":2}]'
Output: [1,5,"false",{"a":2}]
Explanation: Returns the array represented by the JSON string.

Use Cases of JSON.parse()
In this question, we are essentially implementing our own version of the built-in JavaScript function JSON.parse() from scratch. The JSON.parse() function is a crucial utility in JavaScript for converting JSON formatted strings into JavaScript objects. Given the prevalence of JSON in web and application development, understanding the inner workings of JSON.parse() can offer deeper insights into data handling in JavaScript.

Parsing Server Responses

When making AJAX calls or interacting with APIs, the data sent back from the server is often in JSON format. To use this data in our JavaScript applications, we can utilize the response.json() method when working with the Fetch API. This method internally uses JSON.parse() to transform the response body into a JavaScript object.

Note: Always ensure the received data is in valid JSON format to avoid errors during parsing.

fetch('https://api.example.com/data')
.then(response => response.json())
.then(data => {
    console.log(data);
})
.catch(error => console.error('Error:', error));
Local Storage Data Retrieval

Web browsers provide local storage capabilities where data is stored as strings. When storing objects or arrays, they are first converted to JSON strings. When retrieving this data, JSON.parse() can be used to get the data back in its original format.

const user = {
    name: 'John Doe',
    age: 30
};

// Storing data
localStorage.setItem('user', JSON.stringify(user));

// Retrieving data
const retrievedData = localStorage.getItem('user');
const parsedUser = JSON.parse(retrievedData);
console.log(parsedUser);
Configuration Files Reading

Many applications use configuration files in JSON format. To apply these configurations in a JavaScript environment, the file contents are parsed using JSON.parse().

const fs = require('fs');

fs.readFile('/path/to/config.json', 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading the file:', err);
        return;
    }

    const config = JSON.parse(data);
    console.log(config);
});
*/


/*
Approach 1: Recursive Descent Parsing
Intuition
In this problem, our goal is to implement our own version of the built-in JavaScript method, JSON.parse().

Our custom implementation will employ a recursive descent parsing technique to navigate and interpret the structure of the given JSON string. This approach will allow us to delve deeper into nested objects and arrays, and convert them into their respective JavaScript representations.

Algorithm
Initialize a pointer i to traverse the string.
Begin with the parseValue function that will act as a dispatcher. Depending on the current character, it will decide which type of value needs to be parsed (e.g., object, array, string, number, or keyword) and potentially call itself or other parsing functions recursively.
For parsing numbers:
Check for an optional negative sign.
Parse digits for the integer part.
If a decimal point is encountered, parse digits for the fractional part.
Convert the substring corresponding to the number into a JavaScript number using the built-in Number constructor.
For parsing strings:
Look for the starting and ending double quotes. Extract the value in between as the string.
For parsing objects:
Look for opening and closing curly braces.
Within the braces, strings followed by colons indicate keys, and the values after the colons can be any valid JSON values (object, array, string, number, or keyword).
Repeat for each key-value pair and add them to the resultant object.
For parsing arrays:
Look for opening and closing square brackets.
Values within the brackets are separated by commas and can be any valid JSON values.
Repeat for each value and add them to the resultant array.
For parsing keywords (true, false, and null):
Match the exact keyword and return the corresponding JavaScript value.
As the parsing progresses, move the pointer i accordingly to keep track of the current position in the string.
If all operations succeed, return the parsed JavaScript value or object. If there's a mismatch or unexpected character, throw an appropriate error.
By employing recursive descent parsing, this approach elegantly handles nested structures and ensures accurate conversion of the JSON string to its JavaScript counterpart.
*/

var jsonParse = function(str) {
  let i = 0;

  return parseValue();

  function parseValue() {
     switch (str[i]) {
        case '"':
           return parseString();
        case '{':
           return parseObject();
        case '[':
           return parseArray();
        case 't':
        case 'f':
        case 'n':
           return parseLiteral();
        default:
           return parseNumber();
     }
  }

  function parseNumber() {
     let start = i;

     if (str[i] === '-') {
        i++;
     }

     while (i < str.length && isDigit(str[i])) {
        i++;
     }

     if (str[i] === '.') {
        i++;
        while (i < str.length && isDigit(str[i])) {
           i++;
        }
     }

     return Number(str.slice(start, i));
  }

  function isDigit(n) {
     return n >= '0' && n <= '9';
  }

  function parseString() {
     let result = '';
     i++;

     while (i < str.length && str[i] != '"') {
        result += str[i];
        i++;
     }

     i++;
     return result;
  }

  function parseObject() {
     i++;

     const result = {};

     while (i < str.length && str[i] !== '}') {
        const key = parseString();
        expectChar(':');
        const value = parseValue();

        result[key] = value;
        if (str[i] === ',') {
           i++;
        }
     }

     i++;
     return result;
  }

  function parseArray() {
     i++;

     const result = [];

     while (i < str.length && str[i] !== ']') {
        const value = parseValue();
        result.push(value);
        if (str[i] === ',') {
           i++;
        }
     }

     i++;
     return result;
  }

  function parseLiteral() {
     if (str.startsWith('true', i)) {
        i += 4; // length of 'true'
        return true;
     } else if (str.startsWith('false', i)) {
        i += 5; // length of 'false'
        return false;
     } else if (str.startsWith('null', i)) {
        i += 4; // length of 'null'
        return null;
     }
  }

  function expectChar(char) {
     if (str[i] !== char) {
        throw new Error(`Expected '${char}' at position ${i}`);
     }
     i++;
  }
}


/*
Interview Tips:
Can you explain the structure of a JSON string?

A JSON (JavaScript Object Notation) string is a lightweight data-interchange format that is easy for humans to read and write. It is easy for machines to parse and generate. A JSON can contain objects (unordered sets of key-value pairs), arrays (ordered lists of values), numbers, strings, booleans (true or false), and null.
What challenges can arise when parsing a JSON string without using built-in functions?

Parsing a JSON string manually can be challenging due to the nested structures of objects and arrays. Care must be taken to handle the different data types correctly, maintain the hierarchy of nested structures, and manage potential edge cases.
How do you differentiate between different data types in a JSON string, such as objects, arrays, numbers, and strings?

Differentiating between data types in a JSON string involves recognizing specific characters or sequences. Objects start and end with { and }, arrays with [ and ], strings are enclosed in double quotes, numbers are digits that may include a decimal point or negative sign, and booleans are represented by the keywords true and false.
Why might the recursive descent parsing technique be suitable for this problem?

Recursive descent parsing is a top-down parsing technique that starts with the highest-level syntax rule and recursively breaks down the input into its components. Given that a JSON structure is inherently hierarchical with potential nested objects and arrays, recursive descent parsing is a natural fit for such structures. It allows for a straightforward approach to break down and process the nested components of the JSON string.
How do you handle potential edge cases or malformed JSON strings?

For this specific problem, we can assume the input string is a valid JSON string. However, in a real-world scenario, it's essential to handle unexpected characters, unmatched braces or brackets, and other malformed structures by throwing appropriate errors or providing meaningful feedback to the user.
 */