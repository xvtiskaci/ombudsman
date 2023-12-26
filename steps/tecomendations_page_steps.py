from pages.recomendations.add_recommendation_page import AddRecommendationPage
from pages.recomendations.recomendations_page import RecommendationsPage


class RecommendationsPageSteps:
    @staticmethod
    def add_recommendation():
        recommendation_page = RecommendationsPage()
        assert recommendation_page.is_visible()
        recommendation_page.add_recommendation()
    @staticmethod
    def is_recommendation_added():
        recommendations_page_pager = RecommendationsPage()
        add_rec_page = AddRecommendationPage()
        assert add_rec_page.is_visible()
        add_rec_page.click_rec_menu()
        add_rec_page.click_rec_all()
        assert recommendations_page_pager.is_visible()
        page_list = recommendations_page_pager.get_rec_pages()
        last_page = page_list[len(page_list) - 1]
        last_page.click()
        added_rec_list = recommendations_page_pager.get_added_rec()
        last_rec = added_rec_list[len(added_rec_list) - 1]
        last_rec.click()
