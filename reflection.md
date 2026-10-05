# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The hints were not correct, and led me towards the wrong path. It says to go higher when I actually need to go lower and vice versa. Some guesses do not make sense. Like, it tells me to go higher than 99 but lower than 100.
- List at least two concrete bugs you noticed at the start  
  1. says to go higher when I actually need to go lower and vice versa.
  2. When I click on New Game, my previous guess is still in the text box. It needs to be cleared out.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior    | Actual Behavior | Console Output / Error |
|-------|----------------------|-----------------|------------------------|
|   50  | Go higher            | Go lower        |No error, but wrong hint|
|  1500 |Guess is out of range | Go higher       |Not checking for valid input|
|Level hard|Higher range than normal|Half the range of normal|                 |
|New Game|Start a new game     |New game does not start if the previous game ended on a win or if the user ran out of attempts| |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI suggested that the he messages and their emojis are reversed, so they had to be reversed. This was correct, and I verified it by asking AI to write tests and running them, and also manually checking it on the game itself.

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I asked AI to add test cases to verify that the expected behavior was achieved, and also manually tested it in the game.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
