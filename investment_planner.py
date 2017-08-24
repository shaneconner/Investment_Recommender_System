class Questionnaire:


    """
    Attributes:
    age: age of investor.
    retirement_age: expected retirement age of the investor.
    investment_style: investor's 1-10 score where 1 is the most conservative
    and 10 the most risky.
    crash_reaction: investor's reaction to a crash.

    Methods:
    ask_age: asks the investor their age and returns feedback for invalid
    answers.
    ask_retirement_age: asks the investor their expected retirement age and
    returns feedback for invalid answers.
    ask_investment_style: asks the investor their 1-10 score where 1 is the
    most conservative and 10 the most risky and returns feedback for invalid
    answers.
    """


    def __init__(self):


        questions = [self.ask_age, \
                     self.ask_retirement_age, \
                     self.ask_investment_style, \
                     self.ask_crash_reaction]

        # Iterate through each question's function to launch question specific
        # feedback until a valid answer is returned for each or the user quits
        i = 0
        while i < len(questions):
            answered = questions[i]()
            if str(answered).lower() == "quit":
                raise Exception("Exiting program per 'quit' command.")
            if answered is True:
                i += 1
            else:
                continue


    # Verifies user's age input
    def ask_age(self):

        # Request user's age, provide feedback and reiterate question for
        # invalid responses
        self.age = input("What is your age?"
                      + "\nAnswer: ")

        try:
            # Check minimum and maximum age bound intrusions
            # As a general rule, the FLSA sets 14 years of age as the minimum
            # age for employment
            # https://www.dol.gov/general/topic/youthlabor/agerequirements
            if int(self.age) < 14:
                print("Aren't you a tad young for investments? Enjoy your " + \
                    + "\nyouth!"
                    + "\n...or enter an age older than 14 or type 'quit' to " \
                    + "\nexit the program.\n")

            # https://en.wikipedia.org/wiki/List_of_the_verified_oldest_people
            elif int(self.age) > 122:
                print("Unless you're Jeanne Calment the provided age is not" \
                     + "\nvalid. Please enter an age under 122 or type" \
                     + "\n'quit' to exit the program.\n")

            # If no errors, return age attribute as int and green light answer
            else:
                self.age = int(self.age)
                return True

        # For any other errors, return except and if not 'quit', cycle over
        except:

            if str(self.age).lower() != "quit":
                print("Please enter a valid age in an integer format" \
                     + "\n(e.g., 35) or type 'quit' to exit the program.\n")

            else:
                return self.age


    # Verifies user's retirement age input
    def ask_retirement_age(self):

        self.retirement_age = input("\nAt what age do you plan to retire?"
                                 + "\nAnswer: ")

        # Return feedback for minimum and maximum age bound intrusions
        try:

            # Ensure user's retirement age is under 35
            if int(self.retirement_age) <= 35:
                print("But the fun just started! Please enter a retirement" \
                     + "\nage greather than 35 or type 'quit' to exit the" \
                     + "\nprogram.")

            # Ensure retirement age is under 75 if user is under 65
            elif int(self.retirement_age) > 75 and self.age < 65:
                print("You're the glass half empty type, eh? Please enter a" \
                     + "\nretirement age less than 75 or type 'quit' to exit" \
                     + "\nthe program.")

            # If retirement age is younger than their current age, assume user
            # is already retired
            elif int(self.retirement_age) <= self.age:
                self.retirement_age = -1
                return True

            # If no errors result, green light valid answer
            else:
                self.retirement_age = int(self.retirement_age)
                return True

        # If exception resulted, check if user entered quit or recycle question
        except:
            if str(self.retirement_age).lower() != "quit":
                print("Please enter a valid age in an integer format" \
                     + "\n(e.g., 65) or type 'quit' to exit the program.")
            else:
                return self.retirement_age


    # Verifies user's investment style input
    def ask_investment_style(self):

        # Request user's investment style, provide feedback and reiterate
        # question for invalid responses
        self.investment_style = input("\nOn a scale of 1-10, what is your" \
                                     + "\npreferred investment style? (i.e.," \
                                     + "\n1 is the most conservative and 10" \
                                     + "\nthe most aggressive.)"
                                     + "\nAnswer: ")

        # Return feedback for minimum and maximum bound intrusions
        try:
            # Ensure value is at least 1
            if int(self.investment_style) < 1:
                print("Noone is that cautious! Please enter a value greater" \
                     + "\nthan 0 or type 0 to quit.")

            # Ensure value is at most 10
            elif int(self.investment_style) > 10:
                print("I respect your ambition but please enter a value" \
                     + "\ngreater than 0 or type 0 to quit.")

            # If an integer returns within the range, green light valid answer
            else:
                return True

        # If exception resulted, check if user entered quit or recycle question
        except:

            if str(self.investment_style).lower() != "quit":
                print("Please enter a number between 1 and 10 or type 'quit'" \
                     + "\nto exit the program.")

            else:
                return self.investment_style


    # Verify user's reaction to a market crash input
    def ask_crash_reaction(self):

        self.crash_reaction = input("\nIn the event of a market crash, " \
                                    + "how do you react?" \
                                    + "\na) Sell all of the remaining " \
                                    + "investment." \
                                    + "\nb) Sell a portion of the remaining " \
                                    + "investment." \
                                    + "\nc) Hold onto the investment and " \
                                    + "sell nothing." \
                                    + "\nd) Buy more of the investment." \
                                    + "\nAnswer: ")

        valid_answers = "abcd"
        # Return feedback for minimum and maximum bound intrusions
        try:

            # Ensure user entered a, b, c, or d
            if str(self.crash_reaction).lower() not in valid_answers:
                print("Please select an answer valid answer (i.e., 'a', 'b'," \
                     + "\n'c', or 'd') or type 'quit' to exit the program.")
            # If user entered a, b, c, or d green light answer
            else:
                self.crash_reaction = str(self.crash_reaction).lower()
                return True

        # If exception resulted, check if user entered quit or recycle question
        except:

            if str(self.crash_reaction).lower() != "quit":
                print("Please select an answer valid answer (i.e., 'a', 'b'," \
                     + "\n'c', or 'd') or type 'quit' to exit the program.")

            else:
                return self.crash_reaction.lower()


class Investor_Profile:


    """
    Attributes:
    equity_proportion: proportion of suggested investment in equity based
    on the user's current age, expected retirement age, and risk threshold.
    bond_proportion: proportion of suggested investment in bond based
    on the user's current age, expected retirement age, and risk threshold.
    cash_proportion: proportion of suggested cash or cash equivalents based
    on the user's current age, expected retirement age, and risk threshold.
    profile: bucketed profile of investor (Very Conservative to Very
    Aggressive).
    investment_style: investor's 1-10 score where 1 is the most conservative
    and 10 the most risky.
    crash_reaction: investor's reaction to a crash.

    Methods:
    baseline: determine baseline of suggested investment in equity based on
    current age and retirement age.
    risk_threshold: determine risk threshold based on a user's self described
    investment style and reaction to a market crash
    cash_on_hand: suggests amount of cash or cash equivalents to hold based on
    a user's investment profile.
    """


    def __init__(self, investor):

        # Import the user's responses from the Questionnaire class
        self.investor = investor
        # Establish a baseline of portfolio invested in equity stock
        # based on the user's current and expected retirement age
        self.equity_proportion = self.baseline()
        # Bucket the user into an investor profile and adjust equity allocation
        # as appropriate, results driven largely based on information from:
        # https://smartasset.com/investing/asset-allocation-calculator#8VL52n1Rhe
        self.profile = self.risk_threshold()
        # Establish portfolio invested in cash or cash equivalents
        self.cash_proportion = int(round(self.cash_on_hand(),0))
        # Establish portfolio invested in bonds
        self.bond_proportion = int(100 - self.equity_proportion \
                                       - self.cash_proportion)

        print('\nThank you! According to your responses your approach towards ' \
              + '\ninvesting closest aligns with a(n) {} '.format(self.profile) \
              + 'investment profile.\n' \
              + 'In light of your age, retirement age, and risk threshold an ' \
              + '\napproriate asset allocation is: \n\n' \
              + '{:3}'.format(str(self.equity_proportion) + '% ') \
              + 'Stocks' + '\n' \
              + '{:3}'.format(str(self.bond_proportion) + '% ') \
              + 'Bonds' + '\n' \
              + '{:3}'.format(str(self.cash_proportion) + '% ') \
              + 'Cash' + '\n\n')


    # Determine proportion of investments allocated in stock equity
    def baseline(self):

        # If retired, default 45% equity allocation
        if int(self.investor.retirement_age) == -1:
            return 45

        # Conventional wisdom states 110 - current age is that amount
        # Although that doesn't account for individual retirement age
        # variation. If the average retirement is at 65 which recommends
        # a 45% equity allocation, we will use that as a baseline and add
        # years until retirement
        else:
            return int(self.investor.retirement_age) \
            - int(self.investor.age) + 45


    def risk_threshold(self):

        # Use the investor's self described investment style as a baseline
        # for risk tolerance, double that, and subtract 10 to create a range
        # of -10 to 10
        threshold = (int(self.investor.investment_style) * 2) - 10

        # Further adjust risk tolerance based on their reaction to a market
        # crash (risk aversion)
        if self.investor.crash_reaction == 'a':
            threshold -= 10

        elif self.investor.crash_reaction == 'b':
            threshold -= 5

        elif self.investor.crash_reaction == 'c':
            threshold += 5

        elif self.investor.crash_reaction == 'd':
            threshold += 10

        else:
            raise Exception("Unable to calculate investor's risk threshold.")

        # Adjust equity proportion based on tolerance (range of -20 to 20)
        self.equity_proportion += threshold

        if self.equity_proportion > 90:
            self.equity_proportion = 90

        if self.equity_proportion < 0:
            self.equity_proportion = 0

        # Categorize user's investment style based on tolerance
        if threshold < -12:
            return 'Very Conservative'
        elif threshold <= -4:
            return 'Conservative'
        elif threshold <= 4:
            return 'Moderate'
        elif threshold <= 12:
            return 'Aggressive'
        elif threshold > 12:
            return 'Very Aggressive'
        else:
            raise Exception("Unable to determine investor's profile.")


    # Use the investor's profile to determine amount of cash
    # or cash equivalents.
    def cash_on_hand(self):

        # Return 5% cash on hand if user is moderate to very aggressive
        if self.profile == 'Moderate' \
        or self.profile == 'Aggressive' \
        or self.profile == 'Very Aggressive':
            cash = 5

        # Return a 3/11 split of the remainder after accounting for
        # equity proportion
        elif self.profile == 'Conservative':
            cash = (3/11) * (100 - self.equity_proportion)

        # Return a 3/8 split of the remainder after accounting for
        # equity proportion
        elif self.profile == 'Very Conservative':
            cash = (3/8) * (100 - self.equity_proportion)

        else:
            raise Exception("Unable to determine proportion of cash or " \
                          + "cash equivalents.")

        if cash < 5:
            cash = 5

        return cash


class Integrate:


    """
    Attributes:
    funds: True/False regarding if the recommended investments should contain
    only mutual funds, default set to 'True'.
    etfs: True/False regarding if the recommended investments should contain
    only ETF's (exchange-traded fund), default set to 'False'.
    data: investment data of either mutual funds of ETF's.

    Methods:
    import_funds: reads text file manually loaded into executable folder
    locaton which contains data on mutual funds.
    import_etfs: reads text file manually loaded into executable folder
    locaton which contains data on ETFs.
    expense_percentile: assigns an investment's percentile value (higher is
    better) dependent on its respective expense ratio (lower is better).
    rating_percentile: assigns an investment's percentile value (higher is
    better) dependent on its respective Morningstar rating (higher is better).
    rank: averages expense and rating percentiles together and ranks investments
    based on the outcome.
    """


    def __init__(self, funds=False, etfs=False, category=None):

        # If true, imports mutual fund data
        self.funds = funds
        # If true, imports mutual fund data
        self.etfs = etfs

        # Filters to asset category based on given argument
        self.category = category

        # Checks which investment to gather
        if self.funds is True:
            self.data = self.import_funds()

        if self.etfs is True:
            self.data = self.import_etfs()

        # Assigns a percentile value for expense ratio
        self.expense_percentile()
        # Assigns a percentile value for Morningstar rating
        self.rating_percentile()
        # Average expense ratio and Morningstar rating percentiles and reranks
        self.rank()


    # Imports mutual fund data
    def import_funds(self):

        # Import the mutual fund data from txt file
        data = []
        with open('mutual_funds.txt') as inputfile:
            for line in inputfile:
                line = line.split('\t')
                row = []
                # Filter unwanted characters encountered
                for i in line:
                    row.append(i.strip('\xa0').strip('\n').strip('%'))
                try:
                    if row[2] == str(self.category):
                        data.append([row[0], row[1], row[2], \
                                    float(row[6]), int(row[8])])
                    else:
                        continue
                except:
                    continue

        return data


    # Imports ETF data
    def import_etfs(self):

        # Import the ETF data from txt file
        data = []
        with open('etfs.txt') as inputfile:
            for line in inputfile:
                line = line.split('\t')
                row = []
                # Filter unwanted characters encountered
                for i in line:
                    row.append(i.strip('\xa0').strip('\n').strip('%'))
                try:
                    if row[2] == str(self.category):
                        data.append([row[0], row[1], row[2], \
                                    float(row[6]), int(row[3])])
                    else:
                        continue
                except:
                    continue

        return data


    # Assigns a percentile value for expense ratio
    def expense_percentile(self):

        # Sorts data list of lists by expense ratio, lower is better
        self.data.sort(key=lambda x: x[3], reverse=False)

        # Cycles through list of lists, removes any investments without
        # expense ratio information and appends a percentile
        i = 0
        while i < len(self.data):

            # Remove investments with invalid information
            try:
                if self.data[i][3] < 0.01:
                    del self.data[i]
                    continue

            except:
                del self.data[i]
                continue

            # If first value, assign top percentile value (1)
            if i == 0:
                self.data[i].append(1 - (i / len(self.data)))

            # If the expense ratio matches the previos entry's expense ratio,
            # assign the same percentile value
            elif self.data[i][3] == self.data[i-1][3]:
                self.data[i].append(self.data[i-1][5])

            # Otherwise, append percentile by taking 1 minus the percent of
            # investments sorted before current investment
            else:
                self.data[i].append(1 - (i / len(self.data)))

            i += 1


    # Assigns a percentile value for Morningstar rating
    def rating_percentile(self):

        # Sorts data list of lists by Morningstar rating, higher is better
        self.data.sort(key=lambda x: x[4], reverse=True)

        # Cycles through list of lists, removes any investments without
        # Morningstar Rating information and appends a percentile
        i = 0
        while i < len(self.data):

            # Remove investments with invalid information
            try:
                if int(self.data[i][4]) < 1 \
                or int(self.data[i][4]) > 5:
                    del self.data[i]
                    continue

            except:
                del self.data[i]
                continue

            # If first value, assign top percentile value (1)
            if i == 0:
                self.data[i].append(1 - (i / len(self.data)))

            # If the Morningstar rating matches the previos entry's Morningstar
            # rating, assign the same percentile value
            elif self.data[i][4] == self.data[i-1][4]:
                self.data[i].append(self.data[i-1][6])

            # Otherwise, append percentile by taking 1 minus the percent of
            # investments sorted before current investment
            else:
                self.data[i].append(1 - (i / len(self.data)))

            i += 1


    # Average expense ratio and Morningstar rating percentiles and reranks
    def rank(self):

        # Cycles through list of lists, removes any investments unable to add
        # expense ratio percentile and Morningstar rating percentile
        i = 0
        while i < len(self.data):

            # Remove investments resulting in any errors otherwise appends
            # average percentile
            try:
                self.data[i].append((self.data[i][5] + self.data[i][6]) / 2)
                i += 1

            except:
                del self.data[i]
                continue

        # Resorts list of lists by average percentile value
        self.data.sort(key=lambda x: x[7], reverse=True)


class Elaborate(Integrate):


    """
    Attributes:
    portfolio: contains suggested asset allocations and percentage of
    recommended allocation for the user's investment portfolio.
    elaborations: cycles through questions to the user regarding how and to what
    degree to further supply suggestions.

    Methods:
    suggest_allocations: asks user if they would like additional detail
    on the suggested asset allocations and returns feedback for inaccurate
    answers.
    equity_allocation: determines what proportion of a user's portfolio
    should be invested in equity.
    suggest_investments: returns actual investments in the form of mutual funds
    or ETF's based on the user's response. Returns feedback for invalid answers.
    """


    def __init__(self, profile):

        # Imports user profile data
        self.profile = profile
        # Creates blank dictionary for asset allocations to be added to
        self.portfolio = {}
        # Defaults corporate bond for bonds since that is the only recommended
        # type of bond per SmartAssets
        self.portfolio['Corporate Bond'] = self.profile.bond_proportion
        # Defaults cash since it is simply available cash to the user
        self.portfolio['Cash'] = self.profile.cash_proportion

        # List of suggestions to cycle through until valid answer is returned
        elaborations = [self.suggest_allocations, self.suggest_investments]

        # Iterate through each question's function to launch question specific
        # feedback until a valid answer is returned for each or the user quits
        i = 0
        while i < len(elaborations):
            answered = elaborations[i]()
            if str(answered).lower() == 'quit':
                raise Exception("Exiting program, hope this exercise was helpful!")
            if answered is True:
                i += 1
            else:
                continue


    # Asks and computes suggested allocations
    def suggest_allocations(self):

        # Asks user if they would like additional information of asset allocation
        self.allocations = input('Would you like additional asset ' \
                                + 'allocation detail? (yes or no)' \
                                + '\nAnswer: \n')

        # Check for a yes/no or quit answer
        try:

            # If user quits or doesn't request more information, exit program.
            if self.allocations.lower() == 'quit' \
            or self.allocations.lower() == 'n' \
            or self.allocations.lower() == 'no':
                return 'quit'

            # If user returns y, green light allocation computation
            elif self.allocations.lower() == 'yes' \
            or self.allocations.lower() == 'y':
                self.allocations = True

             # For any other errors, cycle over
            else:
                print("Please enter a yes/no answer or type 'quit' to" \
                      + "\nexit the program.\n")

         # For any other errors, return except and if not 'quit', cycle over
        except:

            if str(self.allocations).lower() != "quit":
                print("Please enter a yes/no answer or type 'quit' to" \
                      + "\nexit the program.\n")

            else:
                return self.allocations

        # If green lit and equity is suggested, calculate asset allocation per
        # user's investment profile
        if self.allocations is True \
        and self.profile.equity_proportion > 0:

            if self.profile.profile == 'Very Conservative':
                self.equity_allocation('Large Blend', float(10/20))
                self.equity_allocation('Mid-Cap Blend', float(5/20))
                self.equity_allocation('Foreign Large Blend', float(2.5/20))
                self.equity_allocation('Foreign Small/Mid Blend', float(2.5/20))

            elif self.profile.profile == 'Conservative':
                self.equity_allocation('Large Blend', float(15/45))
                self.equity_allocation('Mid-Cap Blend', float(10/45))
                self.equity_allocation('Small Blend', float(10/45))
                self.equity_allocation('Foreign Large Blend', float(2.5/45))
                self.equity_allocation('Foreign Small/Mid Blend', float(2.5/45))
                self.equity_allocation('Diversified Emerging Mkts', float(5/45))

            elif self.profile.profile == 'Moderate':
                self.equity_allocation('Large Blend', float(20/65))
                self.equity_allocation('Mid-Cap Blend', float(20/65))
                self.equity_allocation('Small Blend', float(10/65))
                self.equity_allocation('Foreign Large Blend', float(5/65))
                self.equity_allocation('Foreign Small/Mid Blend', float(5/65))
                self.equity_allocation('Diversified Emerging Mkts', float(5/65))

            elif self.profile.profile == 'Aggressive':
                self.equity_allocation('Large Blend', float(25/80))
                self.equity_allocation('Mid-Cap Blend', float(20/80))
                self.equity_allocation('Small Blend', float(15/80))
                self.equity_allocation('Foreign Large Blend', float(5/80))
                self.equity_allocation('Foreign Small/Mid Blend', float(5/80))
                self.equity_allocation('Diversified Emerging Mkts', float(10/80))

            elif self.profile.profile == 'Very Aggressive':
                self.equity_allocation('Large Blend', float(20/90))
                self.equity_allocation('Mid-Cap Blend', float(20/90))
                self.equity_allocation('Small Blend', float(20/90))
                self.equity_allocation('Foreign Large Blend', float(7.5/90))
                self.equity_allocation('Foreign Small/Mid Blend', float(7.5/90))
                self.equity_allocation('Diversified Emerging Mkts', float(15/90))

            else:
                print('Unknown error, please try again.')

            print('\nGreat! The following allocation aligns well with your ' \
                 + 'investment profile:\n')

            for key, item in self.portfolio.items():

                print('{category:<30s} \
                       {percentage:<.2f}%'.format(category=key, \
                                                  percentage=item))

            return True


    # Determines proportion of equity per investment category
    def equity_allocation(self, investment_category, proportion):
        self.portfolio[investment_category] = \
            round(float(proportion * self.profile.equity_proportion), 2)


    # Asks user if investments should be recommended and if so, what type
    def suggest_investments(self):

        # Asks user if they would like recommended investments
        self.investments = input('\nWould you like recommended investments ' \
                                + 'for each asset category?' \
                                + '\n(yes or no)' \
                                + '\nAnswer: \n')

        # Check for a yes/no or quit answer
        try:

            # If user quits or doesn't request more information, exit program.
            if self.investments.lower() == 'quit' \
            or self.investments.lower() == 'n' \
            or self.investments.lower() == 'no':
                return 'quit'

            # If user returns yes, green light investment recommendations
            elif self.investments.lower() == 'yes' \
            or self.investments.lower() == 'y':
                self.investments = True

            # Otherwise, recycle through question
            else:
                print("Please enter a yes/no answer or type 'quit' to exit" \
                     + "\nthe program.\n")

        # For any other errors, return except and if not 'quit', cycle over
        except:

            if str(self.investments).lower() != "quit":
                print("Please enter a yes/no answer or type 'quit' to exit" \
                     + "\nthe program.\n")

            else:
                return self.investments

        # If green lit, continue to investment recommendations
        if self.investments is True:

            # Asks user what type of investment (mutual funds or ETFs)
            self.investment_type = input("\nDo you prefer to invest in mutual " \
                                        + "funds or ETF's? Please type 'etf'" \
                                        + "\nif you prefer ETF's or enter any " \
                                        + "other value to return mutual fund" \
                                        + "\ninvestments." \
                                        + '\nAnswer: \n')

            # Default to mutual fund data
            self.etfs = False
            self.funds = True

            # Check if user entered 'ETF'
            try:
                # If user quits or doesn't request more information, exit program.
                if self.investment_type.lower() == 'quit':
                    return 'quit'

                # If user requests ETF, turn ETF to 'True' and turn funds to 'False'
                elif self.investment_type.lower() == 'etf':
                    self.etfs = True
                    self.funds = False

                else:
                    pass

            # For any other errors, return except and if not 'quit', cycle over
            except:

                if str(self.investment_type).lower() != "quit":
                    print("Please enter a yes/no answer or type 'quit' to exit" \
                         + "\nthe program.\n")

                else:
                    return self.investments


            try:

                # Cycle through asset allocations
                for key, item in self.portfolio.items():

                    # Skip over 'Cash' asset allocation
                    if key == 'Cash':
                        continue

                    print('\nTop 5 {category:<30s}'.format(category=key) \
                                + '{percentage:<.2f}%'.format(percentage=item))

                    print('\n{ticker:^10s}'.format(ticker='Ticker') \
                             + '{name:^40s}'.format(name='Name') \
                             + '{expense:^20s}'.format(expense='Expense Ratio') \
                             + '{expense_percentile:^15s}'.format(expense_percentile='Percentile') \
                             + '{rating:^25s}'.format(rating='Morningstar Rating') \
                             + '{rating_percentile:^15s}\n'.format(rating_percentile='Percentile'))

                    data = Integrate(funds=self.funds, etfs=self.etfs, category=str(key))
                    for investment in data.data[:5]:
                        print('{ticker:^10s}'.format(ticker=investment[0]) \
                              + '{name:<40s}'.format(name=investment[1]) \
                              + '{expense:^20.2f}'.format(expense=investment[3]) \
                              + '{expense_percentile:^15.3f}'.format(expense_percentile=investment[5]) \
                              + '{rating:^25d}'.format(rating=investment[4]) \
                              + '{rating_percentile:^15.3f}'.format(rating_percentile=investment[6]))

                print('\n{category:<36s}'.format(category='Cash') \
                      + '{percentage:<.2f}% '.format(percentage=self.portfolio['Cash']) \
                      + '(Savings Account, Money Market, Piggy Bank, etc)')


            except:
                print('Unknown error while retrieving investments.')


            print('\n\nThank you for using this tool, hope the suggestions '
                  + 'are beneficial!')

            return True

user = Questionnaire()
user_profile = Investor_Profile(user)
user_result = Elaborate(user_profile)
