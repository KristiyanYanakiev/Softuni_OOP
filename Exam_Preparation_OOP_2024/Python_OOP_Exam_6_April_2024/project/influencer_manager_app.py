from typing import List, Dict

from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign


class InfluencerManagerApp:
    VALID_INFLUENCER_TYPES: List[str] = ["PremiumInfluencer", "StandardInfluencer"]
    VALID_CAMPAIGN_TYPES: List[str] = ["HighBudgetCampaign", "LowBudgetCampaign"]

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float) -> str:

        if influencer_type not in self.VALID_INFLUENCER_TYPES:
            return f"{influencer_type} is not an allowed influencer type."
        try:
            next(filter(lambda i: i.username == username, self.influencers))
            return f"{username} is already registered."
        except StopIteration:
            if influencer_type == "PremiumInfluencer":
                created_influencer = PremiumInfluencer(username, followers, engagement_rate)
            else:
                created_influencer = StandardInfluencer(username, followers, engagement_rate)

            self.influencers.append(created_influencer)
            return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float) -> str:

        if campaign_type not in self.VALID_CAMPAIGN_TYPES:
            return f"{campaign_type} is not a valid campaign type."
        try:
            next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
            return f"Campaign ID {campaign_id} has already been created."
        except StopIteration:
            if campaign_type == "HighBudgetCampaign":
                created_campaign = HighBudgetCampaign(campaign_id, brand, required_engagement)
            else:
                created_campaign = LowBudgetCampaign(campaign_id, brand, required_engagement)

            self.campaigns.append(created_campaign)
            return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int) -> str or None:
        try:
            influencer: BaseInfluencer = next(filter(lambda i: i.username == influencer_username, self.influencers))
        except StopIteration:
            return f"Influencer '{influencer_username}' not found."

        try:
            campaign: BaseCampaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
        except StopIteration:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return (f"Influencer '{influencer_username}' does not meet the eligibility criteria "
                    f"for the campaign with ID {campaign_id}.")

        if influencer.calculate_payment(campaign) > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= influencer.calculate_payment(campaign)
            influencer.campaigns_participated.append(campaign)

            return (f"Influencer '{influencer_username}' "
                    f"has successfully participated in the campaign with ID {campaign_id}.")

    def calculate_total_reached_followers(self) -> Dict:
        final_dict = {}

        for c in self.campaigns:
            for i in c.approved_influencers:
                final_dict[c] = final_dict.get(c, 0) + i.reached_followers(c.__class__.__name__)

        # for i in self.influencers:
        #     for c in i.campaigns_participated:
        #         final_dict[c] = final_dict.get(c, 0) + i.reached_followers(c.__class__.__name__)

        return final_dict




    def influencer_campaign_report(self, username: str) -> str:

        influencer: BaseInfluencer = next(filter(lambda i: i.username == username, self.influencers))

        if not influencer.campaigns_participated:
            return f"{username} has not participated in any campaigns."

        return influencer.display_campaigns_participated()

    def campaign_statistics(self):

        sorted_campaigns = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), - c.budget))

        res = "$$ Campaign Statistics $$\n"

        for c in sorted_campaigns:
            res += (f"  * Brand: {c.brand}, "
                    f"Total influencers: {len(c.approved_influencers)}, "
                    f"Total budget: ${c.budget:.2f}, "
                    f"Total reached followers: "
                    f"{sum(i.reached_followers(c.__class__.__name__) for i in c.approved_influencers)}\n")

        return res[:-1]
