# DeveloperBuddy
Amazon Alexa Skill to Assist in the generation of code. Currently supports Python only. Eventual support for Java, Ruby, Javascript in that order. 

## Possible out-of-box Queries

- **Alexa please comment lines <line_number_1> through <line_number_2>**
- **Alexa delete line <line_number>**
- **Alexa select line <line_number>**
- **Alexa please select lines <line_number_1> through <line_number_2>**
- **Alexa (un)comment line <line_number>**
- **Alexa (un)comment lines <line_number_1> to <line_number_2>**
- **Alexa redo/undo**
- **Alexa help**

## Adding an sublime existing command

Steps:
1. Write a sublime command is a single function
1. Create an intent schema and some sample utterances
1. Add them via the add_custom_command function
	- params: sublime_function (string as python code), intent schemas (as an array of strings), sample utterances (as an array of strings)
	- `sublime.view.run_command("add_custom_command", "args";{"sublime_function":..., "intent_schemas":[...], "sample_utterances":[...]})`

## Additional Features to Add
**When I have time...**
- Errors and Usage statistics for each command (improve usage)
- Triggers... Look for a pattern and predict usage of command execution
- Suggestions - Can we suggest that you use a command based on the context?
- Custom Commands that can be added from a website online
- Top of List and Featured List- can we list the top used commands on our platform for download?
- Website for easily activating commands
- Priviledged Commands - pay to use certain commands or exclusive access
- File structure creation for coding classes through Alexa command
- Local Database or Cache to try out new commands from Alexa
- "Whats the shortcut for that?" feature

## Contact

If you would like to make any comments or suggestions please feel free to email me at neeasthana@gmail.com

## References 

- https://daanlenaerts.com/blog/2015/06/03/create-a-simple-http-server-with-python-3/
- http://docs.sublimetext.info/en/latest/extensibility/plugins.html
- http://www.sublimetext.com/docs/plugin-examples
- https://github.com/henrikpersson/rsub/blob/master/rsub.py
- https://www.sublimetext.com/docs/3/api_reference.html#sublime.View
