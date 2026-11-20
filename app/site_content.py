"""Single source of truth for all FCCE site content."""

SITE_NAME = "FC Consulting Engineers"
SITE_SHORT = "FCCE"
TAGLINE = "Sustainable energy creation"
MOTTO = "The future is green"
EMAIL = "info@fcceconsultingmw.com"
HERO_IMAGE = "/static/img/media/solar-hillside.jpg"

PROJECT_MEDIA = [
    {
        "image": "/static/img/media/african-water-project.jpg",
        "alt": "African worker carrying a large pipe in a rural water project",
        "category": "Water systems",
    },
    {
        "image": "/static/img/media/african-solar-community.jpg",
        "alt": "African woman working beside a traditional rural home",
        "category": "Community infrastructure",
    },
    {
        "image": "/static/img/media/african-industrial-worker.jpg",
        "alt": "African industrial worker in a technical setting",
        "category": "Waste-to-energy",
    },
    {
        "image": "/static/img/media/african-solar-technician.jpg",
        "alt": "African technician installing solar panels on a rooftop",
        "category": "Solar water systems",
    },
    {
        "image": "/static/img/media/african-engineering-team.jpg",
        "alt": "African engineering team reviewing a project blueprint",
        "category": "Power policy",
    },
    {
        "image": "/static/img/media/african-technology-team.jpg",
        "alt": "African technology team collaborating in an office",
        "category": "Energy policy",
    },
    {
        "image": "/static/img/media/black-man-solar.jpg",
        "alt": "Black technician working with a solar panel",
        "category": "Utility-scale solar",
    },
    {
        "image": "/static/img/media/black-solar-engineer.jpg",
        "alt": "Black engineer working on solar energy equipment",
        "category": "Solar microgrid",
    },
    {
        "image": "/static/img/media/african-solar-worker.jpg",
        "alt": "African solar worker supporting renewable energy delivery",
        "category": "Programme review",
    },
    {
        "image": "/static/img/media/african-woman-technology.jpg",
        "alt": "African woman using technology outdoors",
        "category": "Energy evaluation",
    },
    {
        "image": "/static/img/media/african-electrician.jpg",
        "alt": "African female technician working on an electrical control panel",
        "category": "PV design review",
    },
    {
        "image": "/static/img/media/african-construction-team.jpg",
        "alt": "African construction workers building infrastructure",
        "category": "Solar backup",
    },
    {
        "image": "/static/img/media/black-renewable-team.jpg",
        "alt": "Two people silhouetted against wind turbines",
        "category": "Solar-wind hybrid",
    },
    {
        "image": "/static/img/media/black-technician-work.jpg",
        "alt": "Black technician working in a technical environment",
        "category": "Power generation",
    },
    {
        "image": "/static/img/media/black-woman-engineer.jpg",
        "alt": "Black woman engineer in a professional technical setting",
        "category": "Electrical design",
    },
    {
        "image": "/static/img/media/african-field-worker.jpg",
        "alt": "African field worker in a productive rural landscape",
        "category": "Implementation",
    },
]

SERVICE_GROUPS = [
    {"title": "Energy & power", "body": "Feasibility, generation, electrical systems and utility-scale energy advice.", "anchor": "energy"},
    {"title": "Renewable energy", "body": "Solar PV, hybrid systems, microgrids, storage and resource-led design.", "anchor": "renewable"},
    {"title": "Environment", "body": "Environmental assessments, compliance, sustainability and social safeguards.", "anchor": "environment"},
    {"title": "Delivery & assurance", "body": "Project management, audits, due diligence, review and training.", "anchor": "delivery"},
]

SERVICE_MEDIA = [
    {"image": "/static/img/media/african-engineering-team.jpg", "alt": "African engineering team reviewing a project blueprint"},
    {"image": "/static/img/media/african-solar-technician.jpg", "alt": "African technician installing solar panels"},
    {"image": "/static/img/media/african-technology-team.jpg", "alt": "African technology team collaborating in an office"},
    {"image": "/static/img/media/african-electrician.jpg", "alt": "African technician inspecting an electrical control panel"},
    {"image": "/static/img/media/african-field-worker.jpg", "alt": "African field worker assessing a rural project site"},
    {"image": "/static/img/media/african-solar-worker.jpg", "alt": "African worker supporting a solar energy project"},
    {"image": "/static/img/media/black-woman-engineer.jpg", "alt": "Black woman engineer in a technical workplace"},
    {"image": "/static/img/media/african-construction-team.jpg", "alt": "African construction team building infrastructure"},
    {"image": "/static/img/media/african-industrial-worker.jpg", "alt": "African industrial worker at technical equipment"},
    {"image": "/static/img/media/african-solar-community.jpg", "alt": "African community beside a rural renewable-energy setting"},
    {"image": "/static/img/media/african-water-project.jpg", "alt": "African worker carrying pipe for a community water project"},
    {"image": "/static/img/media/africa-solar-landscape.jpg", "alt": "Solar panels across a rural African landscape"},
    {"image": "/static/img/media/africa-power-lines.jpg", "alt": "Power lines across an African landscape"},
    {"image": "/static/img/media/black-renewable-team.jpg", "alt": "Renewable-energy team silhouetted against wind turbines"},
    {"image": "/static/img/media/african-woman-technology.jpg", "alt": "African woman using technology outdoors"},
    {"image": "/static/img/media/black-man-solar.jpg", "alt": "Black solar technician working with a photovoltaic panel"},
    {"image": "/static/img/media/african-wind-energy.jpg", "alt": "Renewable wind-energy infrastructure"},
    {"image": "/static/img/media/solar-hillside.jpg", "alt": "Solar array across a green hillside landscape"},
    {"image": "/static/img/media/community-water.jpg", "alt": "Community water infrastructure in a rural setting"},
    {"image": "/static/img/media/waste-energy.jpg", "alt": "Waste materials prepared for sustainable energy recovery"},
    {"image": "/static/img/media/policy-analysis.jpg", "alt": "Technical policy and project analysis documents"},
    {"image": "/static/img/media/energy-framework.jpg", "alt": "Energy network and policy framework visual"},
    {"image": "/static/img/media/implementation.jpg", "alt": "Engineer reviewing project implementation plans"},
]

NAV = [
    {"label": "Home", "href": "/", "key": "home"},
    {"label": "About", "href": "/about", "key": "about"},
    {"label": "Services", "href": "/services", "key": "services"},
    {"label": "Projects", "href": "/projects", "key": "projects"},
    {"label": "Contact", "href": "/contact", "key": "contact"},
]

OFFICES = [
    {
        "name": "Lilongwe",
        "role": "Headquarters",
        "address_lines": ["Plot No. 43/793, Area 43", "P.O. Box 31208, Lilongwe 3", "Malawi"],
        "phone": "+265 888 107 134",
        "whatsapp": "265888107134",
    },
    {
        "name": "Mzuzu",
        "role": "Regional Office",
        "address_lines": ["Crisis Nursery Road 003", "Chimaliro, Mzuzu", "Malawi"],
        "phone": "+265 992 770 811",
        "whatsapp": "265992770811",
    },
]

STATS = [
    {"value": "2016", "label": "Established in Malawi"},
    {"value": "20+", "label": "Years combined expertise"},
    {"value": "23", "label": "Specialist services"},
    {"value": "16", "label": "Documented projects"},
]

VALUES = [
    {"title": "Professionalism", "body": "Independent, evidence-led engineering advice you can put your name to."},
    {"title": "Sustainability", "body": "Solutions that respect people, budgets and the environment for the long run."},
    {"title": "Quality", "body": "Rigorous design, review and documentation at every stage."},
    {"title": "Efficiency", "body": "Lean systems and lean delivery — more output from every kilowatt and every kwacha."},
    {"title": "Effectiveness", "body": "Outcomes measured against the client’s real objectives, not just deliverables."},
    {"title": "Satisfaction culture", "body": "We treat client satisfaction as a design requirement from day one."},
]

LEADERSHIP = [
    {
        "name": "Eng. Fredrick Munthali",
        "role": "Managing Partner",
        "focus": "Mechanical and Environmental Engineering",
        "experience": "20+ years",
        "image": "/static/img/Mr%20Fredrick%20Munthali.jpg",
        "bio": "Mechanical and environmental engineering specialist in industrial process and engineering, environmental protection and energy engineering.",
        "email": "munthali@fcceconsultingmw.com",
        "linkedin": "https://www.linkedin.com/in/fredrick-munthali-71045932/",
        "facebook": "https://www.facebook.com/fredrick.munthali.7",
        "credentials": [
            "MSc Environmental Engineering — University of Nottingham, United Kingdom",
            "BSc Mechanical Engineering — University of Malawi (The Polytechnic)",
        ],
    },
    {
        "name": "Eng. Dr. Collen Zalengera",
        "role": "Partner",
        "focus": "Electrical Power & Renewable Energy",
        "experience": "10+ years",
        "image": "/static/img/Dr%20Collen%20Zalengera.jpg",
        "bio": "Electrical power and renewable energy expert with more than 10 years of professional experience in the energy sector.",
        "email": "fzalengera@fcceconsultingmw.com",
        "linkedin": "https://mw.linkedin.com/in/eng-dr-collen-zalengera-r-eng-sre-phd-msc-bsc-01830a21",
        "facebook": "https://www.facebook.com/collen.zalengera",
        "credentials": [
            "PhD Renewable Energy Systems Development — Loughborough University, United Kingdom",
            "MSc Renewable Energy Systems Development — Loughborough University, United Kingdom",
            "BSc Electrical Engineering — University of Malawi (The Polytechnic)",
        ],
    },
]

SERVICES = [
    {"slug": "feasibility-studies", "title": "Feasibility studies", "body": "Technical, financial and environmental viability assessments for energy and infrastructure projects.", "detail": "We test whether a project is worth building before capital is committed: resource assessment, technology options, capital and operating cost estimates, tariff and revenue modelling, and sensitivity analysis. The output is a clear go / no-go recommendation with the evidence behind it."},
    {"slug": "system-design", "title": "System design", "body": "Solar PV, hybrid and micro-grid system design from concept to construction-ready drawings.", "detail": "From load profiling and yield simulation through electrical single-line diagrams, layout drawings, specifications and bills of quantities. Designs are engineered to be buildable, operable and maintainable in the local context."},
    {"slug": "project-management", "title": "Project management", "body": "End-to-end delivery management covering scope, schedule, cost and quality.", "detail": "Owner-side project management: procurement support, contractor coordination, progress and cost control, risk management and reporting. We keep the client informed and the project on its critical path."},
    {"slug": "technical-audits", "title": "Technical audits", "body": "Independent review and audit of existing installations, designs and contractor submissions.", "detail": "Site inspection, performance measurement and document review to confirm whether an installation or design meets its specification. Findings are reported as prioritised, actionable recommendations with indicative costs."},
    {"slug": "environmental-assessments", "title": "Environmental assessments", "body": "ESIA, environmental management plans and statutory compliance support.", "detail": "Environmental and social impact assessment, environmental management plans, stakeholder engagement support and assistance through the statutory approval process in Malawi."},
    {"slug": "energy-audits", "title": "Energy audits", "body": "Consumption analysis and efficiency roadmaps for commercial and industrial facilities.", "detail": "Metering, disaggregation of consumption, benchmarking and identification of efficiency measures ranked by payback. Delivered as a practical roadmap rather than a report that sits on a shelf."},
    {"slug": "design-review", "title": "Design review", "body": "Second-opinion engineering review of third-party designs before capital commitment.", "detail": "An independent check of third-party designs for technical soundness, code compliance, over-specification and buildability, protecting clients from costly design errors before contracts are signed."},
    {"slug": "procurement-support", "title": "Procurement support", "body": "Specifications, bills of quantities and tender evaluation for energy projects.", "detail": "Preparation of technical specifications, BoQs and tender documents, plus structured evaluation of bids against agreed criteria to make procurement defensible and transparent."},
    {"slug": "construction-supervision", "title": "Construction supervision", "body": "Site supervision and quality assurance through commissioning.", "detail": "Site inspections, witness testing, snag management and commissioning oversight to ensure what is built matches what was designed and specified."},
    {"slug": "renewable-energy-advisory", "title": "Renewable energy advisory", "body": "Solar, hydro, biomass and waste-to-energy opportunity assessment.", "detail": "Screening of renewable energy opportunities against resource, site, grid and commercial constraints, with a shortlist of viable options and next steps."},
    {"slug": "energy-access-programmes", "title": "Energy access programmes", "body": "Micro-grid and off-grid programme design for rural and peri-urban communities.", "detail": "Demand assessment, technology selection, tariff and business-model design and implementation planning for community and programme-level energy access."},
    {"slug": "waste-to-energy-advisory", "title": "Waste-to-energy advisory", "body": "Technical and commercial appraisal of waste-to-energy concepts.", "detail": "Assessment of feedstock availability, technology readiness, energy yield and commercial viability, giving clients a realistic view of what a waste-to-energy scheme can deliver."},
    {"slug": "grid-interconnection-studies", "title": "Grid & interconnection studies", "body": "Load studies, interconnection readiness and grid-compliance assessment.", "detail": "Load and generation analysis, interconnection readiness checks and grid-compliance assessment for planned and existing generation projects."},
    {"slug": "training-capacity-building", "title": "Training & capacity building", "body": "Practitioner training on renewable energy design, operation and maintenance.", "detail": "Tailored training for engineers, technicians and programme staff on renewable energy design fundamentals, operation, maintenance and safety."},
    {"slug": "environmental-management", "title": "Environmental management", "body": "Ongoing environmental monitoring and management-plan implementation support.", "detail": "Environmental monitoring, management-plan implementation support and compliance reporting throughout project operation."},
    {"slug": "independent-verification", "title": "Independent verification", "body": "Verification of performance claims, savings and regulatory compliance.", "detail": "Measurement and verification of performance claims and energy savings, and independent confirmation of regulatory compliance for financiers and regulators."},
    {"slug": "due-diligence-reviews", "title": "Due-diligence reviews", "body": "Independent technical and commercial review of renewable energy projects.", "detail": "Technical due-diligence assessment of existing or proposed renewable energy projects, covering design, performance expectations, implementation risk and commercial evidence."},
    {"slug": "statutory-inspections", "title": "Electrical inspections", "body": "Inspection of electrical and renewable energy systems for statutory standard compliance.", "detail": "Site inspection and technical review of electrical and renewable energy installations against statutory standards and applicable project requirements."},
    {"slug": "electrical-fire-safety", "title": "Electrical & fire safety assessments", "body": "Assessment of electrical installations and fire safety risks.", "detail": "Assessment of electrical and fire-safety arrangements, identification of deficiencies and prioritised recommendations for risk reduction and compliance."},
    {"slug": "emissions-accounting", "title": "Emissions accounting", "body": "Greenhouse-gas and emissions accounting for projects.", "detail": "Estimation and documentation of project emissions and avoided emissions to support environmental reporting, planning and investment decisions."},
    {"slug": "waste-management", "title": "Waste management", "body": "Waste management assessment and planning.", "detail": "Waste-arising assessment, management planning and environmental compliance support for projects and facilities."},
    {"slug": "environmental-policies", "title": "Environmental policy drafting", "body": "Development of environmental policies and management frameworks.", "detail": "Drafting of environmental policies and supporting management systems aligned with organisational objectives and regulatory requirements."},
    {"slug": "project-evaluation", "title": "Mid-term & end-of-term evaluation", "body": "Independent evaluation of programme and project delivery.", "detail": "Mid-term and final evaluations assessing implementation, results, delivery effectiveness, sustainability and lessons learned for funders and implementing organisations."},
]

DELIVERABLES = [
    "Technical and economic feasibility reports",
    "Engineering design reports",
    "Detailed design and layout drawings",
    "Project specifications",
    "Bills of quantities",
    "Project briefs",
    "Environmental and social management and monitoring plans",
    "Environmental briefs",
    "Environmental and social impact assessment reports",
    "Training manuals",
    "Competency documentation",
]

CLIENTS = [
    {"title": "Companies", "body": "Private and public companies requiring engineering, energy or environmental advice."},
    {"title": "Public sector", "body": "Government departments, utilities and public agencies delivering national programmes."},
    {"title": "Private sector", "body": "Commercial and industrial organisations investing in reliable, lower-cost energy."},
    {"title": "NGOs", "body": "Non-governmental organisations running energy access and climate programmes."},
    {"title": "Individuals", "body": "Private clients seeking independent technical guidance."},
    {"title": "Country governments", "body": "National programmes and projects implemented across Malawi and the region."},
    {"title": "Financial institutions", "body": "Banks and lenders requiring technical due diligence and verification."},
    {"title": "Insurance companies", "body": "Insurers seeking independent technical assessment and specialist support."},
    {"title": "Development financiers", "body": "Development banks and financing partners investing in sustainable projects."},
    {"title": "Contractors", "body": "Implementation partners requiring design, supervision and technical assurance."},
]

PROJECTS = [
    {"year": "2011–2013", "client": "World Vision", "title": "Maintenance and sustainability assessment of the Malawi World Vision–Danone water supply project", "location": "Zomba and Mzimba, Malawi", "summary": "Maintenance and sustainability assessments of water supply systems powered by photovoltaic solar water pumps."},
    {"year": "2011–2012", "client": "World Vision Malawi", "title": "Sustainability assessment and redesign of solar-powered community water supply systems", "location": "Zomba and Mzimba, Malawi", "summary": "Assessment of solar-powered community water supply systems and development of redesign solutions to improve performance and long-term operation."},
    {"year": "2013–2018", "client": "GEBIS Energy", "title": "Development of a 10 MW waste-to-energy power plant", "location": "Malawi", "summary": "Technical and economic feasibility assessments, environmental studies and financial modelling, including support for Power Purchase Agreement negotiations."},
    {"year": "2014", "client": "World Vision", "title": "Design of a solar-powered water supply system in Dedza", "location": "Dedza, Malawi", "summary": "Design of a solar-powered water supply system and preparation of the schedule of materials required for implementation."},
    {"year": "2015", "client": "Malawi Energy Regulatory Authority", "title": "Power sector regulation and policy analysis", "location": "Malawi", "summary": "Analysis of Malawi’s power sector, focusing on regulatory and policy matters."},
    {"year": "2016", "client": "Oxfam Malawi", "title": "Review of Malawi’s energy policy and legal framework", "location": "Malawi", "summary": "Examination of Malawi’s energy policy and legal framework, identifying gaps and proposing possible solutions."},
    {"year": "2016–2018", "client": "Electricity Generation Company of Malawi", "title": "Development of solar power plants for Likoma and Chizumulu Islands", "location": "Likoma and Chizumulu Islands, Malawi", "summary": "Technical and economic feasibility assessments, engineering design, financial modelling and environmental studies for a 1 MW Likoma Island plant and a 500 kW Chizumulu Island plant."},
    {"year": "2017", "client": "Community Energy Malawi", "title": "Design of an 80 kW solar photovoltaic microgrid for Sitolo Village", "location": "Sitolo Village, Malawi", "summary": "Engineering design, financial modelling and an environmental scoping study for an 80 kW solar photovoltaic microgrid."},
    {"year": "2017", "client": "Practical Action Southern Africa", "title": "Mid-term review of solar microgrid projects in Zimbabwe and Malawi", "location": "Zimbabwe and Malawi", "summary": "Mid-term review of solar microgrid projects ranging from 25 kW to 100 kW under the Sustainable Energy for Rural Communities programme."},
    {"year": "May–June 2017", "client": "Practical Action Southern Africa", "title": "Evaluation of the Sustainable Energy for Rural Communities programme", "location": "Zimbabwe and Malawi", "summary": "Mid-term evaluation of mini-grid-based sustainable energy projects implemented under the Sustainable Energy for Rural Communities (SE4RC) programme."},
    {"year": "2018", "client": "M & E Consulting Engineers", "title": "Review and redesign of the photovoltaic system at the Malawi Energy Regulatory Authority House", "location": "Malawi", "summary": "Review and redesign of the photovoltaic solar power system at the Malawi Energy Regulatory Authority House, with a stated capacity of 72.8 kW."},
    {"year": "2018", "client": "Malawi Revenue Authority", "title": "Energy audit and design of solar backup systems for Malawi Revenue Authority stations", "location": "Malawi", "summary": "Energy audits and design of backup solar photovoltaic systems for 42 Malawi Revenue Authority stations across the country."},
    {"year": "2018", "client": "National Commission for Science and Technology", "title": "Design of a 4 kW solar-wind hybrid system for milk cooling", "location": "Matapwata, Malawi", "summary": "Design of a 4 kW solar-wind hybrid energy system to support milk cooling operations for the Matapwata Bulking Group."},
    {"year": "2018", "client": "UR Energy", "title": "Financial modelling of a 72.8 MW combined-cycle gas turbine and organic Rankine cycle power plant", "location": "Malawi", "summary": "Financial modelling for a proposed 72.8 MW power plant incorporating Combined-Cycle Gas Turbine and Organic Rankine Cycle technologies."},
    {"year": "October–November 2019", "client": "Sempha Investments Co. Ltd", "title": "Electrical design services for Sempha Investments", "location": "Malawi", "summary": "Electrical power calculations, equipment selection, single-line diagrams, bills of quantities and design reports."},
    {"year": "October 2018–September 2019", "client": "Malawi Revenue Authority", "title": "Nationwide energy audits, solar backup system design and installation supervision", "location": "Malawi", "summary": "Joint venture with Prism Consultants. FC Consulting Engineers provided the Team Leader for energy audits, solar system design, ESIA and implementation supervision at all 42 stations and ports."},
]
