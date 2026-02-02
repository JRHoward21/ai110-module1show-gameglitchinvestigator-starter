# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

--- The game looked like a regular guessing game simulator. Two concrete bugs that I noticed was the "new game" reload option didn't work at the end of the guessing. Also, if my answer was higher the secret number it would still say go higher and if it was lower it would still say go lower.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion you accepted and why.
- Give one example of an AI suggestion you changed or rejected and why.

--- For this project I used just AI Copilot. An example of an AI suggestion I used and accepted was a few code grammar suggestions. The AI suggested a more simpler coding structure in the logic_utils.py file. I rejected the change in app.py as it would've changed the structure of the game and it caused failures within the code.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

--- I initially decided whther a bug was fixed by reading over the logic of the code and creating multiple test cases to ensure everything was fixed accurately. A tets I ran manually was the guessing the number feature. I used a number both lower and higher than the secret number to see if it would change from "Go HIGHER" or "Go Lower". AI did help edit and understand the test. The more clear and concisse the question, the better the input was provided by the AI.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

--- The secret number kept changing in the original app because the code was made to generate a new generate a new secret number whenever a new sessions started. Streamlit constantly runs from top to bottom everytime a user interacts with them (clicks a button, moves a slider, types a text). Due to that nothing is remebered by default and the session state is how streamlit remembers things between those reruns. I changed the guessing and the new game function, so you can restart and get a new secret number every in0game session.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

--One habit I want to have from this project is just the ability to run test and take notes on all possible errors. Something I would do differently is see if the AI can provide an easier way to change the code just to check all possible coding options. This project changed how I take AI at a first glace. AI is only as impactful as the user providing the information for it to change. Therefore, the more clear the user and the more information provided, the better the result.