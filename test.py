questions = [
  ('What is the name of the book Hunt for the Wilderpeople is based on? ', 'wild pork and watercress'),
  ('Who was Hunt for the Wilderpeople directed by? ', 'taika waititi'),
  ("How old was Julian Dennison (Ricky Baker) when making Hunt for the Wilderpeople? ", '12'),
  ("True or false, Hunt for the Wilderpeople was the first Aotearoa film to gross over $1M in its first weekend ", 'true'),
  ("Where was Hunt for the Wilderpeople shot? A:Piha  B:Karekare  C:Bethells Beach  D:Horopito E: Kaimawana F: All of the above ", 'f'),
  ("How many weeks did it take to film Hunt for the wilderpeople? A:5 B:13 C:43 ", 'a'),
  ("What word is missing from this famous Hunt for the Wilderpeople quote: I didn't choose the __ life, the __ life chose me! ", 'skux' ),
  ('What franchise did Paula Hall (the police lady) reference when she first found Ricky? ', 'terminator'),
  ("True or false: Ricky named his dog Zag to match Hec's dog, Zig ", 'false'),
  ("True or false: many of the scenes in Hunt for the Wilderpeople were improvised ", 'true'),
  ("What word did Hec make up? ", 'majestical'),
  ("Who played Psycho Sam? ", 'rhys darby'),
  ('How did Bella (the mum) die? A: heart attack B: stroke C: shot D: natural causes', 'b' ),
  ('What decade is Hunt for the Wilderpeople set in? A: 1970s B:2010s C: 1980s D: 1990s', 'c'),
  ("What year did Hunt for the Wilderpeople come out? ", '2016')

] #a list of tuples, each storing a questions the answer
while True: 
  ready = input("Hello, welcome to the quiz all about Hunt for the Wilderpeople! First question: would you like to play? yes or no? ").lower().strip()
  if ready == 'no':
    print('Okay, rerun the program when you are ready!')
    exit() #if the user inputs "no" the quiz ends
  elif ready == 'yes':
    print("Great! Let's get started!") #if the user inputs "yes" it will start the quiz and print 'Great! lets get started!'
    break
  else:
    print('Invalid input, please say yes or no')
while True:
  try:
    num = int(input(f"How many questions would you like? (Max {len(questions)} min 1) ")) #asks the user how many questions they would like and counts the max
    if 1 <= num <= len(questions): #checks if the users input was a vaild number
      break # skips the else if the user input a valid number
    else:
      print('Please enter a valid number')
  except ValueError:
    print("Please enter a valid number") #if the user doesnt input a number itll print 'Please enter a valid number until they do
score = 0 #sets a score
import random
random.shuffle(questions)
for i in range(num): #repeat the loop a set number of times
  q,a = questions[i]
  if input(q + " ").lower() == a: #lowercases the users unput so it will not fail them if they use uppercase letter
    print('Correct!\n')
    score += 1 #adds a point to the score
  else:
    print(f"Incorrect! The answer is '{a}'")
if score >= num / 2:
  print(f"You got {score}/{num}, you pass!")
else:
  print(f"You got {score}/{num}, you fail.")

