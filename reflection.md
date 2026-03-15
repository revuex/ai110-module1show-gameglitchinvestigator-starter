# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  When the difficulty of the game was changed, the range did not match the difficulty level as expected. For example, in the hard mode the range is from 1-50 while for normal mode the range is 1-100

  The game was not updating the banner at the bottom properly based on the input (guess) entered. The game was also showing opposite hint than expected. For example, when guess > secret, it asks users to guess even higher number and vice versa. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used CoPilot. I provided it with context of the code and asked it to identify the logic block that was contributing to the bug. It found the logic block in the codebase and explained to me how the logic is contributing to the bug and steps to resolve it.

I chose to resolve the difficulty bug using AI. In this bug, Hard mode was returning smaller range to guess compared to normal mode; whereas, the hierarchy of difficulty is easy < normal < hard. CoPilot found the logic block that was contributing to the error and suggested steps to resolve it. I used AI to identify the logic block that was handling hierarchy of difficulty and made the changes needed to make this function work correctly.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I ran app.py again to see if the changes have been implemented. I checked manually to see if the difficulty of the game was adjusted. Then, I asked CoPilot to add tests using Pytest to target logic_utils.py. CoPilot helped me understand how pytest works and wrote all necessary tests. 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

Secret number was being randomly generated with each "Submit" clicks because of Streamlit reruns. And, secret number was not being stored for the session. As a result, each time the session refreshed, it generated a new secret number. To resolve this issue, the secret number is being initialized once per game session. 

Imagine that you are trying to solve a substraction problem. For this substraction problem, you have to do a carry-one operation. For sake of reminder, you write down the carry-one on the sidelines of the problem or you remember that you have to carry one. Now take this idea, and bring it to Streamlit. Streamlit is trying to solve a similar substraction problem. Streamlit solves a problem in steps and it forgets when it goes from one step to another. It uses session states to jot down the information from the previous steps and carries it on to the next.  

he key change that gave the game a stable secret number was adding a conditional check to initialize the secret only once per game session. Specifically, the code now uses:
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)
This ensures the secret is generated and stored in Streamlit's session state only when starting a new game, preventing it from resetting on every "Submit" click.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

The habit that I would like to take is to take the time to understand the possible solution and verifying AI generated code. 

I would take the time to sketch out the plan for solution before jumping into the problem.

AI generated code can save time with testing. If you know what you are testing, it is easy to verify the AI outputs. 
