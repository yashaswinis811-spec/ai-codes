# ============================================
# Find-S Algorithm for Concept Learning
# ============================================

def find_s_algorithm(training_data):
    """
    Implementation of the Find-S Algorithm.

    The algorithm finds the most specific hypothesis
    that is consistent with all positive examples.
    """

    # Start with the most specific hypothesis
    hypothesis = ["Ø"] * (len(training_data[0]) - 1)

    print("\nInitial Hypothesis:")
    print(hypothesis)

    # Process each training example
    for example in training_data:

        attributes = example[:-1]
        target = example[-1]

        # Consider only positive examples
        if target == "Yes":

            print("\nPositive Example:")
            print(attributes)

            for i in range(len(attributes)):

                # If hypothesis is still empty
                if hypothesis[i] == "Ø":
                    hypothesis[i] = attributes[i]

                # If values are different, generalize
                elif hypothesis[i] != attributes[i]:
                    hypothesis[i] = "?"

            print("Updated Hypothesis:")
            print(hypothesis)

    return hypothesis


def main():

    print("==============================================")
    print("       FIND-S ALGORITHM")
    print("       Concept Learning")
    print("==============================================")

    # Training dataset
    # Attributes:
    # Sky, AirTemp, Humidity, Wind, Water, Forecast
    #
    # Target:
    # EnjoySport

    training_data = [
        ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes"],
        ["Sunny", "Warm", "High", "Strong", "Warm", "Same", "Yes"],
        ["Rainy", "Cold", "High", "Strong", "Warm", "Change", "No"],
        ["Sunny", "Warm", "High", "Strong", "Cool", "Change", "Yes"]
    ]

    print("\nTraining Dataset:")
    print("----------------------------------------------")

    print("Sky\tAirTemp\tHumidity\tWind\tWater\tForecast\tEnjoySport")

    for row in training_data:
        print(
            f"{row[0]}\t"
            f"{row[1]}\t"
            f"{row[2]}\t"
            f"{row[3]}\t"
            f"{row[4]}\t"
            f"{row[5]}\t\t"
            f"{row[6]}"
        )

    # Apply Find-S Algorithm
    final_hypothesis = find_s_algorithm(training_data)

    print("\n==============================================")
    print("Final Hypothesis:")
    print(final_hypothesis)
    print("==============================================")


if __name__ == "__main__":
    main()
