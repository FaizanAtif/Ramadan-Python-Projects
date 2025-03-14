from fastapi import FastAPI
import random

app = FastAPI()

side_hustles = [
    "Freelancing - Start offering your skills online!",
    "Dropshipping - Sell without handling inventory!",
    "Stock Market - Invest and watch your money grow!",
    "Affiliate Marketing - Earn by promoting products!",
    "Crypto Trading - Buy and sell digital assets!",
    "Online Courses - Share your knowledge and earn!",
    "Print-on-Demand - Sell custom-designed products!",
    "Blogging - Create content and earn through ads and sponsorships!",
    "YouTube Channel - Monetize videos through ads and sponsorships!",
    "Social Media Management - Manage accounts for brands and influencers!",
    "App Development - Create mobile or web applications for businesses!",
    "Virtual Assistant - Help businesses with administrative tasks remotely!",  
    "Etsy Shop - Sell handmade or digital products online!",  
    "Podcasting - Share your voice and earn through sponsorships!",  
    "Amazon KDP - Publish and sell eBooks with zero inventory!",  
    "Video Editing - Offer editing services to content creators and businesses!",  
    "Voiceover Work - Use your voice for ads, audiobooks, and videos!",  
    "SEO Consulting - Help websites rank higher on search engines!",  
    "Website Flipping - Buy, improve, and sell websites for profit!",  
    "Photography - Sell your photos online or work as a freelancer!",  
    "Local Service Business - Offer cleaning, pet sitting, or handyman services!",  

    
    
]


money_quotes = [
        "The way to get started is to quit talking and begin doing. – Walt Disney,",  
    "Formal education will make you a living; self-education will make you a fortune. – Jim Rohn,",  
    "If you don’t find a way to make money while you sleep, you will work until you die. – Warren Buffett,",  
    "Do not save what is left after spending, but spend what is left after saving. – Warren Buffett,",  
    "Money is a terrible master but an excellent servant. – P.T. Barnum,",  
    "You must gain control over your money or the lack of it will forever control you. – Dave Ramsey,",  
    "Opportunities don’t happen. You create them. – Chris Grosser,",  
    "Don’t stay in bed unless you can make money in bed. – George Burns,",  
    "Money often costs too much. – Ralph Waldo Emerson,",  
    "Never depend on a single income. Make an investment to create a second source. – Warren Buffett,",  
    "It’s not about having lots of money. It’s about knowing how to manage it. – Anonymous,",  
    "Rich people have small TVs and big libraries, and poor people have small libraries and big TVs. – Zig Ziglar,",  
    "Being rich is having money; being wealthy is having time. – Margaret Bonnano,",  
    "A wise person should have money in their head, but not in their heart. – Jonathan Swift,",  
    "Money grows on the tree of persistence. – Japanese Proverb,",  
    "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau,",  
    "Do what you love and the money will follow. – Marsha Sinetar,",  
    "Act as if what you do makes a difference. It does. – William James,",  
    "Your income is directly related to your philosophy, not the economy. – Jim Rohn,",  
    "The more you learn, the more you earn. – Warren Buffett,",  
    "An investment in knowledge pays the best interest. – Benjamin Franklin,",  
    "The goal isn’t more money. The goal is living life on your terms. – Chris Brogan,",  
    "Work like you don’t need the money. Love like you’ve never been hurt. Dance like nobody’s watching. – Satchel Paige,",  
    "Financial freedom is available to those who learn about it and work for it. – Robert Kiyosaki,",  
    "Money is like oxygen. You need it to breathe, but it shouldn’t be the purpose of life. – Anonymous,"  

]


@app.get("/side_hustles")
def get_side_hustles():
    """Returns a random side hustle idea"""
    return {"side_hustle": random.choice(side_hustles)}


@app.get("/money_quotes")
def get_money_quotes():
    """Returns a random money quote"""
    return {"money_quote": random.choice(money_quotes)}