from io import StringIO
import loopy_new as lp
import sys

class TestFunctions():

    def test_recipe_scaler_no_ingredients(self):
        assert lp.recipe_scaler([], 2) == []

    def test_recipe_scaler_single_ingredient(self):
        assert lp.recipe_scaler([100], 2) == [200]

    def test_recipe_scaler_multiple_ingredients(self):
        assert lp.recipe_scaler([50, 100, 25], 3) == [150, 300, 75]

    def test_recipe_scaler_half_recipe(self):
        assert lp.recipe_scaler([200, 100, 50], 0.5) == [100, 50, 25]

    def test_recipe_scaler_no_scaling(self):
        assert lp.recipe_scaler([10, 20, 30], 1) == [10, 20, 30]

    def test_recipe_scaler_stress_test(self):
        test_cases = [
            ([25, 50, 75, 100], 4, [100, 200, 300, 400]),
            ([10, 20, 30], 2.5, [25, 50, 75]),
            ([80, 160], 0.25, [20, 40]),
        ]

        for ingredients, multiplier, expected in test_cases:
            assert lp.recipe_scaler(ingredients, multiplier) == expected

    def test_temperature_converter_empty_list(self):
        assert lp.temperature_converter([]) == []

    def test_temperature_converter_single_temp(self):
        assert lp.temperature_converter([0]) == [32]

    def test_temperature_converter_multiple_temps(self):
        assert lp.temperature_converter([0, 100, -40]) == [32, 212, -40]

    def test_temperature_converter_room_temp(self):
        assert lp.temperature_converter([20, 25, 30]) == [68, 77, 86]

    def test_temperature_converter_negative_temps(self):
        assert lp.temperature_converter([-10, -20, -30]) == [14, -4, -22]

    def test_temperature_converter_stress_test(self):
        test_cases = [
            ([37, 40, 50], [98, 104, 122]),
            ([-273, 0, 100], [-459, 32, 212]),
            ([15, 25, 35], [59, 77, 95]),
        ]

        for celsius, expected_fahrenheit in test_cases:
            assert lp.temperature_converter(celsius) == expected_fahrenheit

    def test_password_strength_correct_first_try(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', StringIO('StrongP@ss123\n'))
        captured_output = StringIO()
        sys.stdout = captured_output
        lp.password_strength()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        assert 'Strong password accepted!' in output

    def test_password_strength_weak_then_strong(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', StringIO('weak\nStrongP@ss123\n'))
        captured_output = StringIO()
        sys.stdout = captured_output
        lp.password_strength()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        assert output.count('Enter a password:') == 2
        assert 'Too weak. Try again.' in output
        assert 'Strong password accepted!' in output

    def test_password_strength_multiple_weak_attempts(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', StringIO('abc\n123\nweak\nGoodP@ss1\n'))
        captured_output = StringIO()
        sys.stdout = captured_output
        lp.password_strength()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        assert output.count('Enter a password:') == 4
        assert output.count('Too weak. Try again.') == 3
        assert 'Strong password accepted!' in output

    def test_grade_analyzer_empty_list(self):
        assert lp.grade_analyzer([]) == "No Pass"

    def test_grade_analyzer_all_passing(self):
        assert lp.grade_analyzer([70, 80, 90, 75]) == "Pass"

    def test_grade_analyzer_all_failing(self):
        assert lp.grade_analyzer([30, 45, 55, 59]) == "No Pass"

    def test_grade_analyzer_mixed_grades(self):
        assert lp.grade_analyzer([80, 50, 90, 40]) == "No Pass"

    def test_grade_analyzer_exactly_60(self):
        assert lp.grade_analyzer([60, 60, 60]) == "Pass"

    def test_grade_analyzer_edge_cases(self):
        test_cases = [
            ([59, 60, 61], "No Pass"),
            ([100, 90, 80, 70], "Pass"),
            ([0, 100], "No Pass"),
            ([65, 70, 75, 80], "Pass"),
        ]

        for grades, expected in test_cases:
            assert lp.grade_analyzer(grades) == expected

    def test_valley_finder_empty_list(self):
        assert lp.valley_finder([]) == []

    def test_valley_finder_no_valleys(self):
        assert lp.valley_finder([5, 4, 3, 2, 1]) == []

    def test_valley_finder_single_valley(self):
        assert lp.valley_finder([5, 2, 7]) == [2]

    def test_valley_finder_multiple_valleys(self):
        assert lp.valley_finder([10, 3, 8, 2, 9, 1, 7]) == [3, 2, 1]

    def test_valley_finder_no_edge_valleys(self):
        assert lp.valley_finder([1, 5, 2, 6, 3]) == [2]

    def test_valley_finder_plateau(self):
        assert lp.valley_finder([5, 2, 2, 5]) == []

    def test_valley_finder_stress_test(self):
        test_cases = [
            ([8, 4, 9, 3, 7, 2, 6], [4, 3, 2]),
            ([10, 5, 10, 5, 10], [5, 5]),
            ([3, 1, 4, 1, 5, 9, 2, 6], [1, 1, 2]),
            ([100, 50, 100], [50]),
        ]

        for data, expected in test_cases:
            assert lp.valley_finder(data) == expected

    def test_email_validator_valid_single(self):
        assert lp.email_validator(['test@example.com']) == {
            'valid_emails': ['test@example.com'],
            'invalid_emails': []
        }

    def test_email_validator_invalid_single(self):
        assert lp.email_validator(['notanemail']) == {
            'valid_emails': [],
            'invalid_emails': ['notanemail']
        }

    def test_email_validator_mixed(self):
        emails = [
            'user@domain.com',
            'invalid.email',
            'another@test.org',
            'bad@',
        ]
        result = lp.email_validator(emails)
        assert result == {
            'valid_emails': ['user@domain.com', 'another@test.org'],
            'invalid_emails': ['invalid.email', 'bad@']
        }

    def test_email_validator_empty(self):
        assert lp.email_validator([]) == {
            'valid_emails': [],
            'invalid_emails': []
        }

    def test_email_validator_complex_cases(self):
        test_cases = [
            (
                ['john.doe@company.com', 'jane_smith@university.edu'],
                {'valid_emails': ['john.doe@company.com', 'jane_smith@university.edu'], 'invalid_emails': []}
            ),
            (
                ['@missing.com', 'nodomain@', 'good@email.net'],
                {'valid_emails': ['good@email.net'], 'invalid_emails': ['@missing.com', 'nodomain@']}
            ),
            (
                ['test@domain.co.uk', 'invalid', 'user@site.info'],
                {'valid_emails': ['test@domain.co.uk', 'user@site.info'], 'invalid_emails': ['invalid']}
            ),
        ]

        for emails, expected in test_cases:
            assert lp.email_validator(emails) == expected

    def test_budget_tracker_no_expenses(self):
        assert lp.budget_tracker(1000, []) == "Budget surplus: R 1000"

    def test_budget_tracker_under_budget(self):
        assert lp.budget_tracker(500, [100, 150, 200]) == "Budget surplus: R 50"

    def test_budget_tracker_exact_budget(self):
        assert lp.budget_tracker(300, [100, 100, 100]) == "Budget balanced perfectly!"

    def test_budget_tracker_over_budget_day_1(self):
        assert lp.budget_tracker(100, [150, 50, 25]) == "Budget exceeded on day 1!"

    def test_budget_tracker_over_budget_day_3(self):
        assert lp.budget_tracker(200, [50, 75, 100, 50]) == "Budget exceeded on day 3!"

    def test_budget_tracker_zero_budget(self):
        assert lp.budget_tracker(0, [10, 20]) == "Budget exceeded on day 1!"

    def test_budget_tracker_stress_test(self):
        test_cases = [
            (1000, [200, 300, 400], "Budget surplus: R 100"),
            (500, [500], "Budget balanced perfectly!"),
            (250, [100, 100, 100], "Budget exceeded on day 3!"),
            (600, [150, 150, 150, 150], "Budget balanced perfectly!"),
            (300, [100, 100, 50, 75], "Budget exceeded on day 4!"),
        ]

        for budget, expenses, expected in test_cases:
            assert lp.budget_tracker(budget, expenses) == expected