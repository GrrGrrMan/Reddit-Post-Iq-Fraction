import re

def count_numbers_and_phrases(text):
    # Find all numbers in the text
    numbers = re.findall(r'\b\d+\b', text)
    numbers = list(map(int, numbers))

    # Count numbers strictly greater than 130
    count_above_130 = sum(1 for num in numbers if num >= 130 and num < 300)

    # Count total phrases (defined as ending with 'Share')
    # We'll split by 'Share' and count how many times it appears
    total_phrases = text.count("Share")

    # Avoid division by zero
    fraction = f"{count_above_130}/{total_phrases}" if total_phrases > 0 else "N/A"

    return count_above_130, total_phrases, fraction


# Example usage
sample_text = """Skip to main content
What is your iq? : r/intj


r/intj
Current search is within r/intj

Remove r/intj filter and expand search to all of Reddit
Search in r/intj
Advertise on Reddit

Open chat
Create
Create post
Open inbox

User Avatar
Expand user menu
Skip to NavigationSkip to Right Sidebar

Back
r/intj icon
Go to intj
r/intj
•
9 hr. ago
LapisLazuli_peppers

What is your iq?
Question
Just the title. I’m aware personality doesn’t necessarily determine intelligence. This is just for fun :)


Upvote
11

Downvote

173
Go to comments


Share
Join the conversation
Sort by:

Best

Search Comments
Expand comment search
Comments Section
u/Eggmarine avatar
Eggmarine
•
8h ago
In tests 130. In reality about 19.

track me


Upvote
62

Downvote

Reply
reply

Award

Share

Still-View
•
1h ago
felt this


Upvote
2

Downvote

Reply
reply

Award

Share


Dull_Analyst269
•
6h ago
SunRevolutionary6524
•
8h ago
INTJ - nonbinary
Profile Badge for the Achievement Top 1% Commenter Top 1% Commenter
I scored at 140, but I'm still a dumbass, so 💁



Upvote
32

Downvote

Reply
reply

Award

Share

M_Davis_fan
•
8h ago
I’m not smart; I just think a lot.



Upvote
11

Downvote

Reply
reply

Award

Share

u/CuteYak4406 avatar
CuteYak4406
•
6h ago
INTP
Reaalllll


Upvote
2

Downvote

Reply
reply

Award

Share


1 more reply
Beneficial-Text7830
•
2h ago
135….so I’m a bigger dumbass!


Upvote
2

Downvote

Reply
reply

Award

Share


1 more reply
ayhme
Cake icon
•
8h ago
Don't care. 🤷🏽‍♂️



Upvote
49

Downvote

Reply
reply

Award

Share

u/Classic-Wind-437 avatar
Classic-Wind-437
•
6h ago
INTJ - Teens
happy cake day


Upvote
3

Downvote

Reply
reply

Award

Share

u/LapisLazuli_peppers avatar
LapisLazuli_peppers
OP
•
8h ago
I respect that


Upvote
3

Downvote

Reply
reply

Award

Share

LavaBender93
•
8h ago
INTJ - 30s
I tested at 143 when I was 9. I’ve also got the whole 2e thing going on, being AuDHD, and having alphanumeric and auditory dyslexia, among a few other things.


Upvote
14

Downvote

Reply
reply

Award

Share


1 more reply
u/OxCrow avatar
OxCrow
•
8h ago
INTJ - 20s
107



Upvote
13

Downvote

Reply
reply

Award

Share

u/WombRaider_3 avatar
WombRaider_3
•
7h ago
The only honest person here.



Upvote
5

Downvote

Reply
reply

Award

Share

LavaBender93
•
7h ago
INTJ - 30s
How do you know he’s the only honest person here? Do you know everyone here personally to be able to say with confidence he’s the only honest person here? Lol


Upvote
7

Downvote

Reply
reply

Award

Share

u/Dissasterix avatar
Dissasterix
•
8h ago
I know my number. Its a nice number. But it doesn't mean anything. My parents had me tested as a teen because they thought I was handicapped (poor school performance). I was tested in a clinic. They results were great, but the end-results were not the best. It went to my head, and I cared even less about proving myself. I think knowing this number begat more negative effects than not knowing. And I'm not even impervious to my own stupidity. Bug number, still big dummy.

Don't trust people who only took online tests (the real test was actually pretty hands-on), and NEVER trust someone who cannot display humility.



Upvote
24

Downvote

Reply
reply

Award

Share

Cito_Vorleone
•
2h ago
Are you me?


Upvote
2

Downvote

Reply
reply

Award

Share


2 more replies
u/ForRobotsByRobots avatar
ForRobotsByRobots
•
8h ago
INTJ
Why does this post have Orange font?



Upvote
-1

Downvote

Reply
reply

Award

Share

Andr0NiX
•
8h ago
INTJ
It's a reddit web bug and happens at random to random posts.
Besides, why not ask this as a top level comment?



Upvote
3

Downvote

Reply
reply

Award

Share

u/ForRobotsByRobots avatar
ForRobotsByRobots
•
5h ago
INTJ
I was joking because this sounds like Trump wrote it.


Upvote
2

Downvote

Reply
reply

Award

Share

u/LapisLazuli_peppers avatar
LapisLazuli_peppers
OP
•
7h ago
I like your user name 😆



Upvote
1

Downvote

Reply
reply

Award

Share

u/ForRobotsByRobots avatar
ForRobotsByRobots
•
5h ago
INTJ
Thanks. Im and intj who makes music through robots so it seemed fitting.


Upvote
2

Downvote

Reply
reply

Award

Share

u/Sea_Improvement6250 avatar
Sea_Improvement6250
•
7h ago
INTJ - 40s
144 school age then 136 in my 30s. Now, I'll be thrilled if it goes to 11. 🤘


Upvote
8

Downvote

Reply
reply

Award

Share

Smarmellatissimoide
•
7h ago
It's over 9000



Upvote
7

Downvote

Reply
reply

Award

Share

u/LapisLazuli_peppers avatar
LapisLazuli_peppers
OP
•
7h ago
This made my day. I love dragon ball :))



Upvote
2

Downvote

Reply
reply

Award

Share

Smarmellatissimoide
•
6h ago
•
Edited 5h ago
Glad you got the ref. I also found this, which you may find interesting and less prone to survivorship bias than asking for IQ scores in the INTJ sub. I'm not aware of the existence of other similar studies. Sad they didn't use the WAIS or a more established psychometric battery, although it correlates fairly highly with it. https://sci.bban.top/pdf/10.1177/1073191196003003004.pdf

Comment Image

Upvote
3

Downvote

Reply
reply

Award

Share


3 more replies

1 more reply
duvagin
•
8h ago
i got measured at around 124 many years ago. nowadays i am more open to being ignorant of things that i don’t care about… like IQ tests


Upvote
6

Downvote

Reply
reply

Award

Share


1 more reply
EverthJT4
•
8h ago
INFJ
120, With a 99% percentile in spatial memory, a 97% percentile in logic and a 46% in numerical memory. But they're not really that important, the important thing is to strive for what you want or like.


Upvote
5

Downvote

Reply
reply

Award

Share

u/WombRaider_3 avatar
WombRaider_3
•
7h ago
Room temperature



Upvote
5

Downvote

Reply
reply

Award

Share

u/Shasilison avatar
Shasilison
•
50m ago
INTJ - ♀
i came here to say the exact same thing wtf


Upvote
Vote
Downvote

Reply
reply

Award

Share

u/imthemissy avatar
imthemissy
•
4h ago
INTJ
Profile Badge for the Achievement Top 1% Commenter Top 1% Commenter
I’m smarter than the average bear… but also the type to miss a street sign while mentally solving an investigation or reverse-engineering someone’s motive.

I do know my IQ, and yeah, it’s above average, but that number doesn’t tell the whole story. IQ tests capture logical and verbal intelligence, maybe a bit of spatial reasoning, but that’s it. They don’t measure intuition, insight, behavioral pattern recognition, or metacognition.

There are at least eight types of intelligence. I can write essays (linguistic), analyze behavior (intrapersonal), detect micro-patterns (logical-mathematical), and mentally construct systems (spatial). But ask me to interpret a social cue in real time (interpersonal), complete a hands-on craft (bodily-kinesthetic), or solve something practical in the moment (practical intelligence), and I’ll short-circuit.

So yes, INTJs tend to test well. But intelligence is much bigger than a number. It’s knowing where it excels, where it falls short, and having the clarity to work with both.


Upvote
5

Downvote

Reply
reply

Award

Share

Transverse_City
•
8h ago
INTJ
136 on the Stanford-Binet (4th edition) administered by a proctor at the local university psychology department for a gifted program for high school students at the university.


Upvote
3

Downvote

Reply
reply

Award

Share

qgecko
•
6h ago
INTJ - 50s
Suggestion: make this a poll. Then people don’t have to answer with their specific score since many seem hesitant. Including me.

I took it in high school on the recommendation of a g&t teacher. I scored well.

My takeaways from the exam were (as a high school student):

I don’t understand how spatial abilities points to intelligence.

Picture and word comparisons seem significantly based on culture.

It just didn’t seem fair.

Shortly after I read Daniel Goldman’s work on Emotional Intelligence and lost faith of IQ testing.



Upvote
3

Downvote

Reply
reply

Award

Share

u/LapisLazuli_peppers avatar
LapisLazuli_peppers
OP
•
2h ago
Yeah I agree with you; I also don’t fully have faith in iq tests. A lot of people commenting on this did indeed seem hesitant, didn’t say their iq, or just said that they don’t care about iq tests. I understand but can’t help but feel a little bad because looking back I can see why my initial question may have seemed obnoxious to some..


Upvote
2

Downvote

Reply
reply

Award

Share

Ok_Physics_4154
•
6h ago
Last time I checked it was 120. I think it is okayish


Upvote
3

Downvote

Reply
reply

Award

Share

Legitimate-Gas-1055
•
8h ago
INTJ - ♀
personally i think iq tests are bullshit and should be considered with a grain of salt. it’s a red flag to me when people put too much value on their iq number. in my experience those people tend to be too focused on their actual number than the skills it takes to prove that number



Upvote
5

Downvote

Reply
reply

Award

Share

youngneega123456789
•
7h ago
-iq tests are bullshit -it’s a red flag to me when people put too much value on their iq number
?



Upvote
-3

Downvote

Reply
reply

Award

Share

Legitimate-Gas-1055
•
7h ago
INTJ - ♀
is this supposed to be a question?



Upvote
4

Downvote

Reply
reply

Award

Share

u/Chemical_Signal7802 avatar
Chemical_Signal7802
•
5h ago
INTJ - 20s
Yes I think they had trouble reading what you wrote and are trying to figure out what those words mean. 🐂


Upvote
2

Downvote

Reply
reply

Award

Share

u/ForRobotsByRobots avatar
ForRobotsByRobots
•
8h ago
INTJ
146 but I'm not too invested in it. The only thing it really helps with is explaining the communication gap between me and average person. Supposedly, your communication range is plus or minus 20 points from your own iq.


Upvote
2

Downvote

Reply
reply

Award

Share

u/InsideContent2824 avatar
InsideContent2824
•
7h ago
In the end it doesn’t really matter because it’s just a number that’s influenced by your surroundings, mood, state of mind (level of clarity), your diet for the day, etc. all these things can and will impact your IQ score on a test, as well as the type of test.

But if you want the number, then take the test. Just don’t openly share the number with people, because it can make them feel inferior if they test lower or start questioning themselves. (And yes, I do know my IQ range. My peers all recognize there’s a ton of raw brain power — they just don’t need to know how much 😉)


Upvote
2

Downvote

Reply
reply

Award

Share

Bookssmellneat
•
3h ago
In Canada if you were in the “gifted” program you tested at 130 min IQ.


Upvote
2

Downvote

Reply
reply

Award

Share

Outside_Truth_1685
•
2h ago
I usually score within 130-140 range but I second the voices here saying it doesn’t mean anything. For instance, my emotional intelligence is probably around 20.


Upvote
2

Downvote

Reply
reply

Award

Share

EEJams
•
8h ago
Never been tested, but i assume somewhere between 120 and 130. I think I'm only smarter than some people because I work harder to learn things than others.



Upvote
4

Downvote

Reply
reply

Award

Share


Icy_Path_6654
•
5h ago
0fox2gv
•
8h ago
INTJ - ♂
2 of the readily accepted current versions of mainstream comprehensive tests pegged me around 140 when I was in my late 20s.

Therapist was working through options to explain my thought patterns, being socially withdrawn/dismissive/disinterested, and being so generally distrusting of everybody and everything..

Once the high IQ and INTJ personality was revealed.. they quickly pushed me off to somebody they believed could work with me.

A few months later, I figured out that I was paying them $70 an hour to be their therapist.. and getting nothing in return.

20 years later.. nothing has changed. Abysmal social skills.. but, you definitely want me on your team for the trivia competition. I got the memory- retention-for-obscure-information gene instead of the patience-and-charisma gene.

I instantly recognize the intent and call people out on their pretentiousness or manipulation.. and they despise me for it.

Being intelligent is a curse.


Upvote
3

Downvote

Reply
reply

Award

Share

OkQuantity4011
•
8h ago
INTJ
High enough that even when I'm pressured to answer that question I still get insulted for saying.

Related to intuition, as far as the Jung/MBTI stuff goes. Related to openness and trait curiosity in practical psych.

I maxed those traits when evaluated.

People who are into MBTI (myself included) have a really hard time classifying me because I display the traits of both INTJ and INFJ pretty dang thoroughly.

I lean towards INTJ, I think; but I don't know or care all that much. Introspection seems to be one of those things that produces diminishing returns. I'm still learning to practice moderation, but I'm learning pretty fast that inspecting others so you can meet their needs is way more productive in ways we don't pay enough attention to.

Hope that answers your real question. 🍻🕊️👍🏽


Upvote
2

Downvote

Reply
reply

Award

Share

u/korektan avatar
korektan
•
8h ago
I've never taken one but I can't see it being high, probably below average


Upvote
1

Downvote

Reply
reply

Award

Share

kyleesi666
•
8h ago
INTJ
148


Upvote
1

Downvote

Reply
reply

Award

Share

u/PolloMagnifico avatar
PolloMagnifico
•
8h ago
INTJ - 30s
Depends on the test, consistently top 2.5%


Upvote
1

Downvote

Reply
reply

Award

Share

chud_meister
•
8h ago
INTJ
I've consistently tested around three standard deviations above the mean but I am beginning to suspect it is going up considering the likely impacts of the rising popularity of tiktok/reel video style media consumption combined with the trend of people outsourcing even simple intellectual loads to LLMs. 

Still, take IQ scores with a big fat grain of salt because they measure IQ, not intelligence per se.



Upvote
0

Downvote

Reply
reply

Award

Share

thearctican
•
6h ago
ENTJ
IQ is “intelligence quotient”. What on earth else would it be a measure of?


Upvote
3

Downvote

Reply
reply

Award

Share


1 more reply
u/Psychological_Play21 avatar
Psychological_Play21
•
6h ago
No way people in this thread are honest. The average iq should be around 100, not 140, which is over 2 SD over the mean.



Upvote
-1

Downvote

Reply
reply

Award

Share

u/LapisLazuli_peppers avatar
LapisLazuli_peppers
OP
•
6h ago
I was literally about to comment on this. Should’ve known that only the people with high iqs would comment..



Upvote
2

Downvote

Reply
reply

Award

Share

sugahack
•
5h ago
I think it is more because they only really test the people who are very smart or very not smart. If you're average, they don't test it


Upvote
1

Downvote

Reply
reply

Award

Share


1 more reply
Timely-Helicopter244
•
8h ago
I've never taken an actual test, but it's somewhere between 140-160 given various factors like SAT results. So nothing exact. I know I'm generally intelligent, but the specific number just does not matter.


Upvote
0

Downvote

Reply
reply

Award

Share

One-Let-2553
•
8h ago
INTJ - 40s
It's a pretty cool number. I am a fan of that number. I consider it like my social security number though, no one else needs to know it!


Upvote
0

Downvote

Reply
reply

Award

Share


2 more replies
Enrichus
•
6h ago
INTJ
Around 120. Could be higher if tested under the right conditions. Had to do a test today for a job application and it placed me near the 90th percentile.


Upvote
0

Downvote

Reply
reply

Award

Share

u/ItalianStallion9069 avatar
ItalianStallion9069
•
8h ago
INTJ - ♂
Years ago i tested at 121 iirc


Upvote
1

Downvote

Reply
reply

Award

Share

CarolRaymond
•
8h ago
141


Upvote
1

Downvote

Reply
reply

Award

Share

Grey_Incubus
•
8h ago
It's low, like super low but some how I scored an INFJ on the personality test.


Upvote
1

Downvote

Reply
reply

Award

Share

0rbital-nugget
•
8h ago
INTJ - 30s
IQ isn’t something I ever think about. The only way an IQ test can be accurate is if everyone in the world takes the same test. Besides, they only test for one type of intelligence.


Upvote
1

Downvote

Reply
reply

Award

Share

u/hollyglaser avatar
hollyglaser
•
8h ago
I was told 130


Upvote
1

Downvote

Reply
reply

Award

Share

u/libertysailor avatar
libertysailor
•
8h ago
Don’t know, and I don’t want to. It would probably do more harm than good.


Upvote
1

Downvote

Reply
reply

Award

Share

hidden-in-plainsight
•
8h ago
INTJ - ♂
20 years ago I tested at 128. If that matters.


Upvote
1

Downvote

Reply
reply

Award

Share

Nymelith
•
8h ago
When i was a teen my mom wanted to test me as she thought i was really smart.

But i didn't want to because i don't perform well under stress, so i have no idea.


Upvote
1

Downvote

Reply
reply

Award

Share

u/goldenrod1956 avatar
goldenrod1956
•
8h ago
INTJ - 60s
Mensa high but not Mensa…


Upvote
1

Downvote

Reply
reply

Award

Share


2 more replies
FacelessDorito
•
7h ago
I personally don’t really like the IQ tests. If I’m stupid or smart, it doesn’t really matter to me. I’m good at what I’m good at and bad at what I’m bad at and can improve and get worse. I feel I’m not too bad though


Upvote
1

Downvote

Reply
reply

Award

Share

Kingston_calipso
•
7h ago
INTJ - Teens
Not really high, I'm really bad at logical things lmao.


Upvote
1

Downvote

Reply
reply

Award

Share

u/thatHermitGirl avatar
thatHermitGirl
•
7h ago
INTJ
No idea. They take too long and I have a strong aversion to longer tests.

Other people's scores don't matter to me either, as long as you're not flat-out dumb irl.


Upvote
1

Downvote

Reply
reply

Award

Share

The43Peculiarity
•
7h ago
145


Upvote
1

Downvote

Reply
reply

Award

Share


2 more replies
Zealousideal-Farm496
•
7h ago
135-140 according to the average scores of 5 fsiq tests


Upvote
1

Downvote

Reply
reply

Award

Share

u/uniquelyunpleasant avatar
uniquelyunpleasant
•
7h ago
Probably average. Never taken the test.


Upvote
1

Downvote

Reply
reply

Award

Share

TheMaze01
•
7h ago
149. Official results.


Upvote
1

Downvote

Reply
reply

Award

Share

u/nonameforyou1234 avatar
nonameforyou1234
•
7h ago
I'm tarded 140


Upvote
1

Downvote

Reply
reply

Award

Share

AppreciativeAsshole
•
7h ago
INTJ - 20s
I do not believe that online tests are truly accurate. I have, however, completed a few out of curiosity. Obtained scores between 144 and 148.


Upvote
1

Downvote

Reply
reply

Award

Share

orioleright
•
6h ago
INTJ - 50s
I could join Mensa, but those people are dumbasses. Listen to Jamie Loftus’ podcast. It’s hilarious. 🤣

Also, IQ tests are baloney, but mine got me some opportunities in school I appreciated, so there’s that.


Upvote
1

Downvote

Reply
reply

Award

Share

u/Nearby-Reindeer-6088 avatar
Nearby-Reindeer-6088
•
6h ago
120-ish


Upvote
1

Downvote

Reply
reply

Award

Share

u/CuteYak4406 avatar
CuteYak4406
•
6h ago
INTP
125 I think but iq is so overrated


Upvote
1

Downvote

Reply
reply

Award

Share

u/CuteYak4406 avatar
CuteYak4406
•
6h ago
INTP
2 million probably



Upvote
1

Downvote

Reply
reply

Award

Share

u/LapisLazuli_peppers avatar
LapisLazuli_peppers
OP
•
6h ago
Sounds about right.


Upvote
2

Downvote

Reply
reply

Award

Share

FormerlyDK
•
6h ago
Was tested in school. All I was told was top 2%.


Upvote
1

Downvote

Reply
reply

Award

Share

perplexedparallax
•
6h ago
Top 2% but it only matters in terms of predicting future success, and tends not to change after age 18, so at this point in my life it is irrelevant. The question should be what are you doing with your number, not what is your number.



Upvote
1

Downvote

Reply
reply

Award

Share

u/LapisLazuli_peppers avatar
LapisLazuli_peppers
OP
•
6h ago
I asked the question out of curiosity to see how many INTJs would be high vs average. It’s a stereotype I’ve seen for a while that INTJs are smarter :)…


Upvote
3

Downvote

Reply
reply

Award

Share


3 more replies
Dalilaemily
•
6h ago
Mensa test 118, other science page 136


Upvote
1

Downvote

Reply
reply

Award

Share

KatharinaZarah
•
6h ago
I’ve scored in the 130s before in non formal assessments but I honestly think it’s a little lower, like 110s or 120s.


Upvote
1

Downvote

Reply
reply

Award

Share

u/Clean_Personality324 avatar
Clean_Personality324
•
6h ago
INTJ
Dude, in my opinion, wanting to know what Iq you are is seen as low intelligence. This may or may not be backed by statistics, but - Big number, Big ego.


Upvote
1

Downvote

Reply
reply

Award

Share


2 more replies
luulitko
•
6h ago
INTJ - 40s
I'm good at language, logic, observation and forming patterns or deduction. I suck at math and I might not deliver reliably similar results each time. And the test didn't even measure everything I'm good at or how I interact with others. This in mind, I don't care that I once got overly optimistic number as result, I might not be at same mood and headspace or nutritional status again. Might have worse, or better.


Upvote
1

Downvote

Reply
reply

Award

Share

u/xp3rf3kt10n avatar
xp3rf3kt10n
•
6h ago
132 from a legit tester when I was young (though my mom only told me the results a few years ago, she has the pictures). Willing to do it again due to a bet between my wife and I lmao... but I am too lazy to go to a site for it. It seems fun though!

If anyone knows an online one that is legit. I am willing to compete with my wife on it hahaha


Upvote
1

Downvote

Reply
reply

Award

Share

thearctican
•
6h ago
ENTJ
I don’t know for sure because I haven’t had a psychologist do a proper evaluation. Because it doesn’t really matter.

The Mensa online test puts me in the high 130s, for what it’s worth.


Upvote
1

Downvote

Reply
reply

Award

Share

TaddThick
•
6h ago
I was tested at 136 in high school.


Upvote
1

Downvote

Reply
reply

Award

Share

Arnaghad_Bear
•
6h ago
INTJ - ♂
I haven't checked since I got my TBI in the military. Before that I scored 156. I think I became a marine to become less intelligent and feel normal though.


Upvote
1

Downvote

Reply
reply

Award

Share

Kentucky_Supreme
•
6h ago
As long as this is anonymous, obviously it's 1 BILLION 😎


Upvote
1

Downvote

Reply
reply

Award

Share


buboniccupcake
•
6h ago
sugahack
•
5h ago
It used to be way up there but I have tried my best to kill as many braincells as possible for much of my adult life, so who knows


Upvote
1

Downvote

Reply
reply

Award

Share

1ntercept0r_Prime
•
5h ago
NGL, I found the test pointless. Classifying people by math logic when the world runs on common sense and emotions makes me go "WTF, how is this useful irl?"


Upvote
1

Downvote

Reply
reply

Award

Share


Elegant-Armadillo-88
•
5h ago
INTJ
NichtFBI
•
5h ago
•
Edited 5h ago
INTJ
I was in the top percentile in multiple things, including mathematics against all 11th grade students in a state with good math scores and a practice IQ thing that they asked a few students to do. But I didn't care about that at all, and I still don't.

If you can practice and study for an intelligence test, then it isn't an intelligence test. But when I was writing a paper on education and the different types of intelligence, I took an enormous amount of open-source testing. I have a low verbal IQ relative to my other areas but am extremely high in others. I particularly don't like the label and prejudice that would come with it. There are people who obsess over their IQ scores, and those people aren't intelligent in the way that matters.

Pairing my DNA with others, I share DNA with others that have "more persistent brain arousal," "stronger memory performance," "likely to exhibit high levels of cognitive dissonance tolerance," "highly adept at pattern recognition," "unlikely to display emotional intelligence," "likely to have higher white matter integrity," "likely to show higher static spatial working memory," "high working memory," "likely to show higher figural fluency," and am "less likely to remember negative or positive interactions."

The rest of them are in the mid category. Except for creativity, and the ability to focus.


Upvote
1

Downvote

Reply
reply

Award

Share

u/abort-alyssa avatar
abort-alyssa
•
5h ago
havent been tested but its probably in the range of 1-299 if i had to guess


Upvote
1

Downvote

Reply
reply

Award

Share

Exciting_Koala_1384
•
5h ago
INTJ - nonbinary
Only losers care about that. It's not even an accurate measure of Intelligence.


Upvote
1

Downvote

Reply
reply

Award

Share

atlanticzid
•
5h ago
120-125 according to the internet, room temperature iq irl


Upvote
1

Downvote

Reply
reply

Award

Share

GagiMarkov
•
5h ago
Of coure you are going to get only high iq anwers here. No one is gonna brag about an average or below average iq. Therefore this question is meaningless if you want to determine how smart INTJs are on average.



Upvote
1

Downvote

Reply
reply

Award

Share

u/LapisLazuli_peppers avatar
LapisLazuli_peppers
OP
•
4h ago
•
Edited 3h ago
I know :((. One of the reasons I posted this was for fun


Upvote
1

Downvote

Reply
reply

Award

Share

Jbwood
•
5h ago
INTJ - 30s
It's been almost 20 years. So the number is way outdated now. What was a good score years ago might be average now.

But ultimately, pattern recognition and memorization skills dont really define intelligence to me. I've have the pleasure to meet people with downs that taught me amazing things and met plenty of doctors in their respective fields of study that didnt seem to know anything else about anything.


Upvote
1

Downvote

Reply
reply

Award

Share


Icy_Path_6654
•
5h ago
MomentarySolace
•
5h ago
INTJ - 30s
133 but it was from a non standardized test back when I was 15 years old.


Upvote
1

Downvote

Reply
reply

Award

Share

sillypelin
•
5h ago
I’m between one and two standard deviations above the mean 😵‍💫


Upvote
1

Downvote

Reply
reply

Award

Share

Aelin017
•
5h ago
145


Upvote
1

Downvote

Reply
reply

Award

Share

u/Tiny-Celebration-838 avatar
Tiny-Celebration-838
•
5h ago
80 if i'm lucky 😆😅 i've come to accept it.


Upvote
1

Downvote

Reply
reply

Award

Share

Fantasy-Shark-League
•
5h ago
139. Evaluation was administered by a school psychologist in 5th grade.


Upvote
1

Downvote

Reply
reply

Award

Share

u/Chemical_Signal7802 avatar
Chemical_Signal7802
•
5h ago
INTJ - 20s
Interesting. I think someone else pointed it out but be sure not to fall into selection bias op. I haven't seen a single person report an iq below 100 which is statistically very unlikely if the selection is a true representation of the population given the sample size of 30 or so reports. People are far less likely to answer this question if they have a poor result.

To get a true population read it would be better to select at random people in r/intj and then Dm or message them to get their iq results. I'm going to check out the paper another commentor shared.


Upvote
1

Downvote

Reply
reply

Award

Share

VSHoward
•
5h ago
INTJ
My sister ordered me a MENSA test a long time ago when I was in my early 20s. I received my results in the mail, and my score was 143. I told everyone I scored a 95. I don’t like any special attention, and didn’t want to make a big deal of it. Thirty years later, most days, 95 feels about spot on. 🤣


Upvote
1

Downvote

Reply
reply

Award

Share

Scary_Bill_4178
•
5h ago
130 but im the dumbest smart person that i know. I do dumb stuff and mess up.


Upvote
1

Downvote

Reply
reply

Award

Share

Endless-reverie
•
4h ago
116


Upvote
1

Downvote

Reply
reply

Award

Share

Dingo_Gab
•
4h ago
INTJ
I don’t want to know tbh lol


Upvote
1

Downvote

Reply
reply

Award

Share

u/Impossible-Cut154 avatar
Impossible-Cut154
•
4h ago
i score 132


Upvote
1

Downvote

Reply
reply

Award

Share

u/Federal_Base_8606 avatar
Federal_Base_8606
•
4h ago
mine is BLUE and triangular


Upvote
1

Downvote

Reply
reply

Award

Share

sociopsych0o
•
4h ago
realistically 100 - 115


Upvote
1

Downvote

Reply
reply

Award

Share

u/Wheeljack26 avatar
Wheeljack26
•
4h ago
INTJ - 20s
137 in mensa test but don't care tbh, I've a lot to improve in a lot of areas, nothing matters anymore


Upvote
1

Downvote

Reply
reply

Award

Share

AimIsInSleepMode
•
3h ago
Once got 70 when and 130 (online)

70 seems more like it


Upvote
1

Downvote

Reply
reply

Award

Share

u/SorryStore4389 avatar
SorryStore4389
•
3h ago
INTJ
200



Upvote
1

Downvote

Reply
reply

Award

Share

u/LapisLazuli_peppers avatar
LapisLazuli_peppers
OP
•
3h ago
That’s real.


Upvote
1

Downvote

Reply
reply

Award

Share

DarknessSOTN
•
3h ago
136, I was tested when I was 11 years old 7 years ago. I think it has only helped me to be a weirdo.


Upvote
1

Downvote

Reply
reply

Award

Share

EarthRocker_
•
3h ago
INTJ - ♂
Unless everyone here took the same, standardised IQ test, comparing numbers is not very informative.

But it can be fun, so I don't want to rain on your parade :)



Upvote
1

Downvote

Reply
reply

Award

Share

u/LapisLazuli_peppers avatar
LapisLazuli_peppers
OP
•
3h ago
One of the reasons I made this post was just cause I was bored and wanted to see what people would put. Unfortunately it was kinda a bad question I feel like haha


Upvote
2

Downvote

Reply
reply

Award

Share

u/FakedAutopsy636 avatar
FakedAutopsy636
•
3h ago
Like around 90 to 113


Upvote
1

Downvote

Reply
reply

Award

Share

u/Mapsgdc avatar
Mapsgdc
•
2h ago
Where do you take your tests?



Upvote
1

Downvote

Reply
reply

Award

Share

u/LapisLazuli_peppers avatar
LapisLazuli_peppers
OP
•
2h ago
Iq tests? Psychologists most likely


Upvote
1

Downvote

Reply
reply

Award

Share

LateRemote7287
•
2h ago
When i was tested last, it was 130. Which is hilarious because I'm nowhere near extremely intelligent. I'm pretty average in all departments.


Upvote
1

Downvote

Reply
reply

Award

Share

keybladenakanojo
•
2h ago
151


Upvote
1

Downvote

Reply
reply

Award

Share

u/the-heart-of-chimera avatar
the-heart-of-chimera
•
2h ago
INTJ - ♂
About 200. I reckon 300 if I post it on social media.


Upvote
1

Downvote

Reply
reply

Award

Share

u/awr90 avatar
awr90
•
2h ago
I took several in college and was always in the 115-120 range. Most people are lying in here.


Upvote
1

Downvote

Reply
reply

Award

Share

u/Agreeable_Round361 avatar
Agreeable_Round361
•
2h ago
I don't know my iq but I'm smarter than everyone


Upvote
1

Downvote

Reply
reply

Award

Share

Karmaswhiskee
•
2h ago
INTJ - ♀
Uhhhhh last time I tested I think I was 13? I believe it was around 116-120? That number has def gone down though because I do the dumbest shit sometimes 😂


Upvote
1

Downvote

Reply
reply

Award

Share

Byrux69
•
2h ago
Do online tests really count? I took one some years ago and I scared 131 (but it was not in my native language, so I guess that could affect the result). Also, I've gotten more st*p¡d over the years lol


Upvote
1

Downvote

Reply
reply

Award

Share

DevilinDeTales
•
2h ago
I forgot what it was but it was higher than my expectations. It didn't change that I still think I'm dumber than the next person. It is kind of nice though when I surprise someone with what I know or can figure out that helps them just because for me it's just random facts or just because I chalk it up to "fresh eyes" or something.

I work retail currently, going back to school within the next year cause I'm finally stable, and every so often dealing with customers is also a reminder too that I am not as dumb I constantly believe I am.


Upvote
1

Downvote

Reply
reply

Award

Share

u/Dependent_Fill5037 avatar
Dependent_Fill5037
•
2h ago
142, but feels lower once I had kids


Upvote
1

Downvote

Reply
reply

Award

Share

u/krivirk avatar
krivirk
•
2h ago
INTJ
Unjokingly more than you'd expect and or guess.


Upvote
1

Downvote

Reply
reply

Award

Share

u/winterweiss2902 avatar
winterweiss2902
•
1h ago
130. 110 when drunk


Upvote
1

Downvote

Reply
reply

Award

Share

u/Changetheworld69420 avatar
Changetheworld69420
•
1h ago
I don’t know what tests to trust so I haven’t taken one tbh. They say Chemical Engineers are I think usually around 130 so that’s just what I tell people🤷‍♂️ although I do have a lot more practical/life knowledge than most ChemE’s I know😂 not sure if that has a positive or negative correlation with IQ though tbh because I had a buddy in college who was a legit genius, and yes he was INTJ as well lol, but holy cow was he useless in a lot of situations😅 like I know when I’m in a room with someone smarter than me, and 95% of the time that dude made me feel it, then we’d have to change a flat tire or something and he was as much help as a bird.


Upvote
1

Downvote

Reply
reply

Award

Share

u/Shasilison avatar
Shasilison
•
1h ago
INTJ - ♀
Room temperature


Upvote
1

Downvote

Reply
reply

Award

Share

LuckySlushy1600
•
1h ago
100 exactly


Upvote
1

Downvote

Reply
reply

Award

Share

u/Ok_Opposite029 avatar
Ok_Opposite029
•
59m ago
INFJ here, it was 98 when I was 13, I'm pretty sure it's much higher now that I have a little more worldly experience. 😅


Upvote
Vote
Downvote

Reply
reply

Award

Share

secretsusi
•
49m ago
130. Tested 20 years ago, going down hill ever since.


Upvote
Vote
Downvote

Reply
reply

Award

Share

Dr_Falkov
•
45m ago
INTJ - ♂
In test 131


Upvote
Vote
Downvote

Reply
reply

Award

Share

Community Info Section
r/intj
Join
analytical, conceptual and objective
For those who score INTJ on the MBTI personality inventory. Check the r/INTJ rules and the FAQ before posting.
Created Nov 21,
Public

Community Guide
Members
50
 Online
User flair
u/Euphoric_Musician_38 avatar
Euphoric_Musician_38
Community Bookmarks
Wiki
r/intj Rules
1
1 - Selfie videos must have a transcript
2
2 - No Memes, No pictures of text
3
3 - Self posts must have self text
Moderators
Message Mods
u/permaculture avatar
u/permaculture
u/Gtt1229 avatar
u/Gtt1229
u/AutoModerator avatar
u/AutoModerator
u/BotDefense avatar
u/BotDefense
u/MAGIC_EYE_BOT avatar
u/MAGIC_EYE_BOT
Magic Eye
u/admin-tattler avatar
u/admin-tattler
u/bot-bouncer avatar
u/bot-bouncer
View all moderators
Installed Apps
Admin Tattler
Bot Bouncer
Languages
Français
Português
Русский
Reddit Rules
Privacy Policy
User Agreement
Accessibility
Reddit, Inc. © . All rights reserved.

Collapse Navigation

"""

count_above_130, total_phrases, fraction = count_numbers_and_phrases(sample_text)

print(f"Numbers > 130: {count_above_130}")
print(f"Total phrases: {total_phrases}")
print(f"Fraction: {fraction}")
