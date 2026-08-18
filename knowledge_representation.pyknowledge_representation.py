# ============================================
# Knowledge Representation using:
# 1. Predicate Logic
# 2. Rule-Based System
# ============================================


# --------------------------------------------
# PART 1: PREDICATE LOGIC
# --------------------------------------------

# Predicate:
# Student(Alice)
# Student(Bob)
# Studies(Alice, AI)
# Studies(Bob, Python)

students = {
    "Alice",
    "Bob",
    "Charlie"
}

studies = {
    ("Alice", "AI"),
    ("Bob", "Python"),
    ("Charlie", "AI")
}

likes = {
    ("Alice", "Python"),
    ("Bob", "AI"),
    ("Charlie", "Python")
}


def predicate_logic_demo():
    print("\n========== PREDICATE LOGIC ==========\n")

    print("Students:")
    for student in students:
        print(f"Student({student})")

    print("\nStudies:")
    for person, subject in studies:
        print(f"Studies({person}, {subject})")

    print("\nLikes:")
    for person, subject in likes:
        print(f"Likes({person}, {subject})")

    # Query 1
    person = "Alice"

    if person in students:
        print(f"\nQuery: Is {person} a student?")
        print("Answer: True")

    # Query 2
    query = ("Alice", "AI")

    if query in studies:
        print(f"\nQuery: Does {query[0]} study {query[1]}?")
        print("Answer: True")
    else:
        print("Answer: False")


# --------------------------------------------
# PART 2: RULE-BASED SYSTEM
# --------------------------------------------

# Facts
facts = {
    "is_student",
    "studies_ai",
    "likes_programming"
}


# Rules:
#
# IF someone is a student
# AND studies AI
# THEN they can learn programming.
#
# IF someone can learn programming
# AND likes programming
# THEN they are a programmer.
#
# IF someone is a programmer
# THEN they can develop software.


rules = [
    {
        "conditions": {"is_student", "studies_ai"},
        "conclusion": "can_learn_programming"
    },

    {
        "conditions": {"can_learn_programming", "likes_programming"},
        "conclusion": "is_programmer"
    },

    {
        "conditions": {"is_programmer"},
        "conclusion": "can_develop_software"
    }
]


def apply_rules(facts, rules):

    new_facts = set(facts)

    changed = True

    while changed:

        changed = False

        for rule in rules:

            conditions = rule["conditions"]
            conclusion = rule["conclusion"]

            # Check whether all conditions are satisfied
            if conditions.issubset(new_facts):

                if conclusion not in new_facts:
                    new_facts.add(conclusion)
                    changed = True

    return new_facts


def rule_based_demo():

    print("\n========== RULE-BASED SYSTEM ==========\n")

    print("Initial Facts:")

    for fact in facts:
        print(f"- {fact}")

    # Apply rules
    final_facts = apply_rules(facts, rules)

    print("\nRules:")

    for i, rule in enumerate(rules, start=1):

        conditions = " AND ".join(rule["conditions"])
        conclusion = rule["conclusion"]

        print(f"Rule {i}:")
        print(f"IF {conditions}")
        print(f"THEN {conclusion}\n")

    print("Derived Knowledge:")

    for fact in final_facts:

        if fact not in facts:
            print(f"- {fact}")

    # Query
    print("\n========== QUERY ==========\n")

    query = "can_develop_software"

    print(f"Query: Can the person develop software?")

    if query in final_facts:
        print("Answer: YES")
    else:
        print("Answer: NO")


# --------------------------------------------
# MAIN PROGRAM
# --------------------------------------------

def main():

    print("==============================================")
    print(" KNOWLEDGE REPRESENTATION")
    print(" Predicate Logic and Rule-Based Systems")
    print("==============================================")

    predicate_logic_demo()

    rule_based_demo()


if __name__ == "__main__":
    main()
