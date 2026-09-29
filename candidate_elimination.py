import csv

def candidate_elimination(data):
    attributes = len(data[0]) - 1

    # Most specific hypothesis
    S = ['0'] * attributes

    # Most general hypothesis
    G = [['?'] * attributes]

    for row in data:
        x = row[:-1]
        label = row[-1]

        if label == 'Yes':
            # Generalize S
            for i in range(attributes):
                if S[i] == '0':
                    S[i] = x[i]
                elif S[i] != x[i]:
                    S[i] = '?'

            # Remove hypotheses from G inconsistent with S
            G = [g for g in G if all(
                g[i] == '?' or g[i] == S[i] or S[i] == '?'
                for i in range(attributes)
            )]

        else:
            # Specialize G
            new_G = []

            for g in G:
                for i in range(attributes):
                    if g[i] == '?':
                        if S[i] != '?' and S[i] != '0':
                            new_h = g.copy()
                            new_h[i] = S[i]
                            new_G.append(new_h)

            G = new_G

    return S, G


data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

S, G = candidate_elimination(data)

print("Specific Hypothesis (S):")
print(S)

print("\nGeneral Hypotheses (G):")
for hypothesis in G:
    print(hypothesis)
