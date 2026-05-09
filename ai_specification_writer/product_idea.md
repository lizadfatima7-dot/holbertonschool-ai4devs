python -c "
content = '''# Product Idea

## Vision
Enable students and developers to track their learning progress, set goals, and get AI-powered study recommendations to accelerate skill development.

## Users
- **Students**: want to organize their learning path, track completed topics, and stay motivated.
- **Developers**: want to identify skill gaps, follow structured roadmaps, and measure progress over time.
- **Mentors**: want to monitor mentee progress and suggest resources based on performance data.

## Key Features
- Personalized learning roadmap builder
- Daily progress tracking with visual dashboards
- AI-powered resource recommendations based on current skill level
- Goal setting with deadline reminders and milestone alerts
- Peer comparison and community leaderboards
- Integration with GitHub to track coding activity automatically
'''
with open(r'C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\ai_specification_writer\product_idea.md', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
"