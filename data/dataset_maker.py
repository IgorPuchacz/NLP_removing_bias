import pandas as pd
import random

# Female
stereotypes_female = [
    "They prefer caregiving roles.",
    "They are overly emotional.",
    "They excel in household tasks.",
    "They avoid confrontation.",
    "They are naturally nurturing.",
    "They talk too much.",
    "They lack technical aptitude.",
    "They are indecisive under pressure.",
    "They prioritize family over career.",
    "They shy away from negotiation.",
    "They are bad at math and science.",
    "They focus on appearance.",
    "They are risk-averse.",
    "They need guidance to take charge.",
    "They are passive listeners.",
    "They get upset easily.",
    "They are better suited for admin work.",
    "They depend on others for direction.",
    "They excel at multitasking domestic chores.",
    "They are sensitive and soft-spoken."
]
anti_stereotypes_female = [
    "They thrive in leadership positions.",
    "They excel at strategic decision-making.",
    "They lead complex projects effectively.",
    "They drive innovation in teams.",
    "They are decisive under pressure.",
    "They master technical subjects easily.",
    "They negotiate tough deals confidently.",
    "They take calculated risks.",
    "They outperform on quantitative tasks.",
    "They set ambitious career goals.",
    "They mentor others in STEM fields.",
    "They excel in competitive sports.",
    "They are outspoken public speakers.",
    "They lead global research initiatives.",
    "They design cutting-edge technology.",
    "They handle high-stress situations calmly.",
    "They build scalable software systems.",
    "They manage large budgets effectively.",
    "They instruct advanced mathematics.",
    "They pioneer scientific breakthroughs."
]

# Male
stereotypes_male = [
    "They excel at strategic planning.",
    "They thrive in leadership roles.",
    "They are outspoken and bold.",
    "They are confident decision-makers.",
    "They focus on career over family.",
    "They avoid emotional discussions.",
    "They prefer hands-on work.",
    "They are naturally competitive.",
    "They take charge in group settings.",
    "They solve technical problems quickly.",
    "They dislike detail-oriented tasks.",
    "They assert their opinions forcefully.",
    "They are risk-takers.",
    "They prioritize strength over empathy.",
    "They handle finances without hesitation.",
    "They are self-reliant.",
    "They resist asking for help.",
    "They fix mechanical issues effortlessly.",
    "They are bad at communication.",
    "They prefer working alone."
]
anti_stereotypes_male = [
    "They are nurturing and empathetic.",
    "They are supportive listeners.",
    "They prefer caregiving roles.",
    "They avoid confrontation.",
    "They excel at organizing domestic chores.",
    "They ask for emotional support when needed.",
    "They thrive in collaborative discussions.",
    "They are sensitive to others’ needs.",
    "They mentor peers in interpersonal skills.",
    "They prioritize work-life balance.",
    "They communicate feelings openly.",
    "They flourish in caregiving professions.",
    "They excel at mediation and compromise.",
    "They seek guidance from mentors.",
    "They handle conflicts with diplomacy.",
    "They value emotional intelligence.",
    "They are detail-oriented in planning events.",
    "They embrace vulnerability as strength.",
    "They collaborate effectively in teams.",
    "They foster nurturing relationships."
]

# Neutral
neutrals = [
    "They appreciate cultural traditions.",
    "They show strong analytical skills.",
    "They foster community learning.",
    "They engage in urban sketching.",
    "They support grassroots initiatives.",
    "They explore theoretical physics.",
    "They contribute to open-source code.",
    "They mentor newcomers in hobbies.",
    "They curate independent film festivals.",
    "They design sustainable gardens.",
    "They write technical documentation.",
    "They organize local book swaps.",
    "They research historical archives.",
    "They teach online masterclasses.",
    "They restore classic cars.",
    "They compose instrumental music.",
    "They manage community workshops.",
    "They moderate educational forums.",
    "They test experimental recipes.",
    "They lead philosophy discussion groups.",
    "They invent custom mechanical puzzles.",
    "They analyze market trends deeply.",
    "They pilot remote-controlled drones.",
    "They build interactive art installations.",
    "They develop citizen science apps.",
    "They host cultural cooking classes.",
    "They coordinate volunteer networks.",
    "They teach coding to seniors.",
    "They record wildlife soundscapes.",
    "They organize charity hackathons.",
    "They author illustrated guidebooks.",
    "They map underwater ecosystems.",
    "They lead mindfulness retreats.",
    "They study comparative literature.",
    "They craft miniature dioramas.",
    "They produce independent podcasts.",
    "They host local music jams.",
    "They create educational videos.",
    "They review academic papers voluntarily."
]

# Names + genders (context)
contexts = [
    ("Mary", "female"),
    ("Jennifer", "female"),
    ("Elizabeth", "female"),
    ("Suzanne", "female"),
    ("Jessica", "female"),
    ("Caren", "female"),
    ("Sarah", "female"),
    ("Lisa", "female"),
    ("Ashley", "female"),
    ("Sandra", "female"),
    ("Emily", "female"),
    ("Michelle", "female"),
    ("Amanda", "female"),
    ("Melissa", "female"),
    ("Rebecca", "female"),
    ("James", "male"),
    ("Michael", "male"),
    ("John", "male"),
    ("Robert", "male"),
    ("David", "male"),
    ("William", "male"),
    ("Richard", "male"),
    ("Thomas", "male"),
    ("Christopher", "male"),
    ("Matthew", "male"),
    ("Mark", "male"),
    ("Donald", "male"),
    ("Paul", "male"),
    ("Kevin", "male"),
    ("Timothy", "male"),
]

rows = []
for _ in range(200):
    ctxt, gender = random.choice(contexts)
    if gender == "female":
        stereo = random.choice(stereotypes_female)
        anti_stereo = random.choice(anti_stereotypes_female)
        label = "1"
    else:
        stereo = random.choice(stereotypes_male)
        anti_stereo = random.choice(anti_stereotypes_male)
        label = "0"

    mean = random.choice(neutrals)

    rows.append({
        "context": ctxt + " is " + gender,
        "stereotype": stereo,
        "anti-stereotype": anti_stereo,
        "meaningless": mean,
        "label": label
    })

df = pd.DataFrame(rows)
df.to_csv("dataset_6.csv", index=False)
print("⚙️ Generated new data")
