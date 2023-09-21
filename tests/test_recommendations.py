from steps.add_rec_page_steps import AddRecPageSteps
from steps.login_page_steps import LoginPageSteps
from steps.tecomendations_page_steps import RecommendationsPageSteps


class TestRecommendations:

    def test_recommendation_should_be_added(self):
        login_steps = LoginPageSteps
        recommendations_page_steps = RecommendationsPageSteps
        add_rec_page_steps = AddRecPageSteps
        login_steps.login()
        recommendations_page_steps.add_recommendation()
        add_rec_page_steps.fill_rec_form()
        recommendations_page_steps.is_recommendation_added()





