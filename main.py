from agents.profile_agent import load_profile
from agents.trend_agent import fetch_trend
from agents.post_writer_agent import generate_post
from agents.approval_agent import approve_post

profile = load_profile()
trend = fetch_trend()

post = generate_post(profile, trend)
approve_post(post)
