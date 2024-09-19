from econ.jobs import job
from econ.attribute import Attribute

jobs = {
    "data scientist" : job.Job(
        name="Data Scientist",
        hourly_pay= 58.0,
        description=("A Data Scientist is a person who is passionate about data and machine learning.\n"
        "They analyze complex data using statistical methods and machine learning techniques to uncover insights, create predictive models, and help businesses make data-driven decisions."),
        requirements = {
            "Strength" : 5.0,
            "Dexterity" : 55.5,
            "Intelligence" : 85.0,
            "Charisma" : 30.0,
            "Creativity" : 20.0,
            "Employability" : 75.0,
            }
        ),
        "software developer" : job.Job(
        name="Software Developer",
        hourly_pay= 65.0,
        description=("A Software Developer is a person who is passionate about developing software.\n"
        "They use programming languages such as Python, C++, C#, Java, and JavaScript to create software applications."),
        requirements = {
            "Strength" : 5.0,
            "Dexterity" : 55.5,
            "Intelligence" : 80.0,
            "Charisma" : 10.0,
            "Creativity" : 45.0,
            "Employability" : 75.0,
            }
        ),
        "economist" : job.Job(
        name="Economist",
        hourly_pay= 38.0,
        description=("An Economist is a person who is passionate about economics and finance.\n"
        "They analyze data and use mathematical models to make predictions about the future."),
        requirements = {
            "Strength" : 10,
            "Dexterity" : 25.0,
            "Intelligence" : 75.0,
            "Charisma" : 50.0,
            "Creativity" : 20.0,
            "Employability" : 50.0,
            }
        ),
        "chef" : job.Job(
        name="Chef",
        hourly_pay= 15.0,
        description=("A Chef is a person who is passionate about cooking.\n"
        "They use ingredients to create delicious dishes."),
        requirements = {
            "Strength" : 40.0,
            "Dexterity" : 70.0,
            "Intelligence" : 30.0,
            "Charisma" : 25.5,
            "Creativity" : 30.0,
            "Employability" : 10.0,
            }
        ),
        "architect" : job.Job(
        name="Architect",
        hourly_pay= 39.0,
        description=("An Architect is a person who is passionate about designing.\n"
        "They use mathematical and geometric methods to create buildings."),
        requirements = {
            "Strength" : 30.0,
            "Dexterity" : 60.0,
            "Intelligence" : 45.0,
            "Charisma" : 35.0,
            "Creativity" : 70.0,
            "Employability" : 45.0,

            }
        ),
        "teacher" : job.Job(
        name="High School Teacher",
        hourly_pay= 33.0,
        description=("A High School Teacher is a person who is passionate about educating teenagers.\n"
        "They use their subject expertise and pedagogical skills to help students learn and prepare for college or careers."),
        requirements = {
            "Strength" : 10.0,
            "Dexterity" : 60.0,
            "Intelligence" : 80.0,
            "Charisma" : 40.0,
            "Creativity" : 10.0,
            "Employability" : 40.0,
            }
        ),
        "nurse" : job.Job(
        name="Nurse",
        hourly_pay= 34.5,
        description=("A Nurse is a person who is passionate about healthcare.\n"
        "They use their knowledge to treat patients."),
        requirements = {
            "Strength" : 30.0,
            "Dexterity" : 70.0,
            "Intelligence" : 60.0,
            "Charisma" : 30.0,
            "Creativity" : 5.0,
            "Employability" : 80.0,
            }
        ),
        "journalist" : job.Job(
        name="Journalist",
        hourly_pay= 14.5,
        description=("A Video-game Journalist is a person who is a useless individual.\n"
        "They use their uselessness to write bad articles about games.\n"
        "if you take this job, you're bad."),
        requirements = {
            "Strength" : 0.0,
            "Dexterity" : 10.0,
            "Intelligence" : 10.0,
            "Charisma" : 10.0,
            "Creativity" : 30.0,
            "Employability" : 0.0,
            }
        ),
        "real estate agent" : job.Job(
        name="Real Estate Agent",
        hourly_pay= 20.69,
        description=("A Real Estate Agent is a person who is passionate about real estate.\n"
        "They use their knowledge to help people buy and sell real estate."),
        requirements = {
            "Strength" : 30.0,
            "Dexterity" : 30.0,
            "Intelligence" : 60.0,
            "Charisma" : 70.0,
            "Creativity" : 10.0,
            "Employability" : 60.0,
            }
        ),
        "cashier" : job.Job(
        name="Cashier",
        hourly_pay= 12.5,
        description=("A Cashier is a person who is passionate about cash.\n"
        "They use their knowledge to help people buy and sell cash."),
        requirements = {
            "Strength" : 5.0,
            "Dexterity" : 15.0,
            "Intelligence" : 5.0,
            "Charisma" : 5.0,
            "Creativity" : 0.0,
            "Employability" : 5.0,
            }
        ),
        "graphic designer" : job.Job(
        name="Graphic Designer",
        hourly_pay= 20.0,
        description=("A Graphic Designer is a person who is passionate about design.\n"
        "They use their knowledge to create beautiful designs."),
        requirements = {
            "Strength" : 20.0,
            "Dexterity" : 30.0,
            "Intelligence" : 20.0,
            "Charisma" : 30.0,
            "Creativity" : 85.0,
            "Employability" : 40.0,
            }
        ),
        "marine biologist": job.Job(
        name="Marine Biologist",
        hourly_pay=45.0,
        description=("A Marine Biologist studies ocean ecosystems and marine life.\n"
                     "They conduct research to understand marine species, their behaviors, and their environments."),
        requirements={
            "Strength": 25.0,
            "Dexterity": 40.0,
            "Intelligence": 80.0,
            "Charisma": 20.0,
            "Creativity": 35.0,
            "Employability": 55.0,
        }
        ),
        "urban planner": job.Job(
        name="Urban Planner",
        hourly_pay=42.0,
        description=("An Urban Planner designs and organizes land use in urban areas.\n"
                     "They create plans and policies for land development, infrastructure, and community services."),
        requirements={
            "Strength": 20.0,
            "Dexterity": 35.0,
            "Intelligence": 70.0,
            "Charisma": 50.0,
            "Creativity": 40.0,
            "Employability": 60.0,
        }
        ),
        "photographer": job.Job(
        name="Photographer",
        hourly_pay=25.0,
        description=("A Photographer captures images through various photographic techniques.\n"
                     "They work on events, portraits, or artistic projects to create visual content."),
        requirements={
            "Strength": 15.0,
            "Dexterity": 50.0,
            "Intelligence": 30.0,
            "Charisma": 40.0,
            "Creativity": 70.0,
            "Employability": 50.0,
        }
        ),
        "mechanical engineer": job.Job(
        name="Mechanical Engineer",
        hourly_pay=50.0,
        description=("A Mechanical Engineer designs and develops mechanical systems and devices.\n"
                     "They apply principles of mechanics, thermodynamics, and materials science to solve engineering problems."),
        requirements={
            "Strength": 35.0,
            "Dexterity": 40.0,
            "Intelligence": 85.0,
            "Charisma": 20.0,
            "Creativity": 30.0,
            "Employability": 65.0,
        }
        ),
        "social media manager": job.Job(
        name="Social Media Manager",
        hourly_pay=28.0,
        description=("A Social Media Manager creates and manages social media content and campaigns.\n"
                     "They use social platforms to engage with audiences and enhance brand presence."),
        requirements={
            "Strength": 10.0,
            "Dexterity": 30.0,
            "Intelligence": 60.0,
            "Charisma": 70.0,
            "Creativity": 50.0,
            "Employability": 55.0,
        }
        ),
        "event coordinator": job.Job(
        name="Event Coordinator",
        hourly_pay=22.0,
        description=("An Event Coordinator plans and organizes events such as weddings, conferences, and parties.\n"
                     "They handle logistics, vendor coordination, and ensure that events run smoothly and meet clients' expectations."),
        requirements={
            "Strength": 15.0,
            "Dexterity": 40.0,
            "Intelligence": 50.0,
            "Charisma": 60.0,
            "Creativity": 45.0,
            "Employability": 50.0,
        }
        ),
        "biochemist": job.Job(
        name="Biochemist",
        hourly_pay=52.0,
        description=("A Biochemist studies the chemical processes and substances in living organisms.\n"
                     "They conduct research to understand biological functions and develop new medical or agricultural products."),
        requirements={
            "Strength": 20.0,
            "Dexterity": 30.0,
            "Intelligence": 85.0,
            "Charisma": 25.0,
            "Creativity": 30.0,
            "Employability": 60.0,
        }
        ),
        "travel agent": job.Job(
        name="Travel Agent",
        hourly_pay=18.0,
        description=("A Travel Agent helps clients plan and book their travel arrangements.\n"
                     "They provide recommendations, manage bookings, and assist with travel-related issues."),
        requirements={
            "Strength": 10.0,
            "Dexterity": 20.0,
            "Intelligence": 45.0,
            "Charisma": 70.0,
            "Creativity": 20.0,
            "Employability": 50.0,
        }
        ),
        "fitness trainer": job.Job(
        name="Fitness Trainer",
        hourly_pay=30.0,
        description=("A Fitness Trainer develops and leads exercise programs to help clients achieve their fitness goals.\n"
                     "They provide guidance on exercises, nutrition, and lifestyle changes."),
        requirements={
            "Strength": 50.0,
            "Dexterity": 45.0,
            "Intelligence": 30.0,
            "Charisma": 50.0,
            "Creativity": 15.0,
            "Employability": 55.0,
        }
        ),
        "content writer": job.Job(
        name="Content Writer",
        hourly_pay=22.0,
        description=("A Content Writer creates written material for websites, blogs, and marketing purposes.\n"
                     "They produce engaging and informative content to attract and retain audiences."),
        requirements={
            "Strength": 5.0,
            "Dexterity": 30.0,
            "Intelligence": 55.0,
            "Charisma": 30.0,
            "Creativity": 60.0,
            "Employability": 50.0,
        }
        ),
        "cybersecurity analyst": job.Job(
        name="Cybersecurity Analyst",
        hourly_pay=55.0,
        description=("A Cybersecurity Analyst protects an organization's computer systems and networks from cyber threats.\n"
                     "They monitor for security breaches, investigate incidents, and implement security measures."),
        requirements={
            "Strength": 10.0,
            "Dexterity": 40.0,
            "Intelligence": 85.0,
            "Charisma": 20.0,
            "Creativity": 25.0,
            "Employability": 70.0,
        }
        ),
        "flight attendant": job.Job(
        name="Flight Attendant",
        hourly_pay=25.0,
        description=("A Flight Attendant ensures the safety and comfort of passengers during flights.\n"
                     "They provide customer service, manage emergencies, and assist with passenger needs."),
        requirements={
            "Strength": 20.0,
            "Dexterity": 50.0,
            "Intelligence": 40.0,
            "Charisma": 80.0,
            "Creativity": 15.0,
            "Employability": 65.0,
        }
        ),
        "landscape architect": job.Job(
        name="Landscape Architect",
        hourly_pay=48.0,
        description=("A Landscape Architect designs outdoor spaces and environments.\n"
                     "They create plans for parks, gardens, and public spaces, integrating aesthetic and functional elements."),
        requirements={
            "Strength": 25.0,
            "Dexterity": 35.0,
            "Intelligence": 70.0,
            "Charisma": 30.0,
            "Creativity": 60.0,
            "Employability": 55.0,
        }
        ),
        "veterinarian": job.Job(
        name="Veterinarian",
        hourly_pay=60.0,
        description=("A Veterinarian diagnoses and treats illnesses and injuries in animals.\n"
                     "They provide medical care, perform surgeries, and offer advice on animal health and nutrition."),
        requirements={
            "Strength": 25.0,
            "Dexterity": 40.0,
            "Intelligence": 85.0,
            "Charisma": 30.0,
            "Creativity": 30.0,
            "Employability": 70.0,
        }
        ),
        "financial analyst": job.Job(
        name="Financial Analyst",
        hourly_pay=43.0,
        description=("A Financial Analyst evaluates financial data to provide investment recommendations and insights.\n"
                     "They analyze trends, create financial models, and assist in decision-making for investments and budgeting."),
        requirements={
            "Strength": 10.0,
            "Dexterity": 25.0,
            "Intelligence": 80.0,
            "Charisma": 20.0,
            "Creativity": 20.0,
            "Employability": 60.0,
        }
        ),
        "art curator": job.Job(
        name="Art Curator",
        hourly_pay=40.0,
        description=("An Art Curator manages and oversees art collections in museums or galleries.\n"
                     "They organize exhibitions, acquire new works, and research art history."),
        requirements={
            "Strength": 15.0,
            "Dexterity": 25.0,
            "Intelligence": 75.0,
            "Charisma": 40.0,
            "Creativity": 50.0,
            "Employability": 55.0,
        }
        ),
        "seo specialist": job.Job(
        name="SEO Specialist",
        hourly_pay=32.0,
        description=("An SEO Specialist improves the visibility of websites in search engines.\n"
                     "They analyze and implement strategies to increase organic search rankings and drive web traffic."),
        requirements={
            "Strength": 10.0,
            "Dexterity": 30.0,
            "Intelligence": 60.0,
            "Charisma": 25.0,
            "Creativity": 35.0,
            "Employability": 55.0,
        }
        ),
        "it support specialist": job.Job(
        name="IT Support Specialist",
        hourly_pay=27.0,
        description=("An IT Support Specialist assists with technical issues and provides support for computer systems and software.\n"
                     "They troubleshoot problems, offer solutions, and maintain IT infrastructure."),
        requirements={
            "Strength": 10.0,
            "Dexterity": 35.0,
            "Intelligence": 60.0,
            "Charisma": 20.0,
            "Creativity": 15.0,
            "Employability": 60.0,
        }
        ),
        "public relations specialist": job.Job(
        name="Public Relations Specialist",
        hourly_pay=35.0,
        description=("A Public Relations Specialist manages an organization's public image and communications.\n"
                     "They create press releases, handle media relations, and develop strategies to maintain a positive public perception."),
        requirements={
            "Strength": 10.0,
            "Dexterity": 30.0,
            "Intelligence": 55.0,
            "Charisma": 70.0,
            "Creativity": 40.0,
            "Employability": 60.0,
        }
        ),
        "janitor": job.Job(    
            name="Janitor",
            hourly_pay=9.5,
            description=("A Janitor is responsible for cleaning and maintaining buildings and facilities.\n"
                            "They perform tasks such as sweeping, mopping, vacuuming, and ensuring overall cleanliness and sanitation."),
            requirements={
                "Strength": 5.0,
                "Dexterity": 5.0,
                "Intelligence": 1.0,
                "Charisma": 1.0,
                "Creativity": 0.0,
                "Employability": 3.0,
        }
        ),
        "fast food worker": job.Job(
        name="Fast Food Worker",
        hourly_pay=8.5,
        description=("A Fast Food Worker prepares and serves food in a fast food restaurant.\n"
                        "They take orders, operate cash registers, and maintain cleanliness in the work area."),
        requirements={
            "Strength": 5.0,
            "Dexterity": 5.0,
            "Intelligence": 2.5,
            "Charisma": 3.0,
            "Creativity": 0.0,
            "Employability": 1.0,
        }
        ),
        "box mover": job.Job(
        name="Box Mover",
        hourly_pay=12.0,
        description=("A Box Mover is responsible for lifting, carrying, and transporting boxes and other items.\n"
                        "They load and unload trucks, organize storage areas, and ensure proper handling of goods."),
        requirements={
            "Strength": 5.0,
            "Dexterity": 5.0,
            "Intelligence": 2.5,
            "Charisma": 3.0,
            "Creativity": 0.0,
            "Employability": 0.0,
        }
        ),
        
}

