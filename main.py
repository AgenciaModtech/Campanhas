from facebook_business.api import FacebookAdsApi
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.user import User
from facebook_business.adobjects.adaccount import AdAccount
import json

fields = [
    'id',
    'name',
    'status',
    'objective',
    'start_time',
    'end_time',
    'created_time',
    'updated_time',
    'budget_rebalance_flag',
    'lifetime_budget',
    'daily_budget',
    'spend_cap',
    'account_id',
    'insights{clicks,cpc,cpm,ctr,reach}'
]

access_token = 'EAAEcmTta5DIBOxFfBeddOiaInW8uL9bH1wTWm3osCZAwLvbpkU5SjqV5zvb8hKl2ae8ERY0usYPTBB7cbt5kZA3gcFvoc62ZBZA9a8yHOMPtjXRYmJIXrejDZAnFWZAjKQI3WGjC9klpZCiQirY1B5iwAh9OUxu4nGiunyajiNwEvI6z5JOkhfWFctV'
app_secret = '2c25cd54585667f2babf816de4eaec56'
app_id = '312919428097074'



FacebookAdsApi.init(access_token=access_token, app_id=app_id, app_secret=app_secret)
me = User(fbid='me')
campaigns_data = []
for account in me.get_ad_accounts(fields=['id']):
    ad_account = AdAccount(account["id"])

    campaigns = ad_account.get_campaigns(fields=fields)
    for campaign in campaigns:
        campaign_dict = campaign.export_all_data()
        insights = campaign.get_insights(fields=[
            'clicks',
            'cpc',
            'cpm',
            'ctr',
            'engagement_rate_ranking',
            'reach',
            'spend',
            'impressions',
        ])
        print(campaign)
        for insight in insights:
            insight_dict = insight.export_all_data()
            combined_data = {**campaign_dict, **insight_dict}
            campaigns_data.append(combined_data)
            
with open('data.json', 'w', encoding="utf-8") as file:
    json.dump(campaigns_data, file)
            


