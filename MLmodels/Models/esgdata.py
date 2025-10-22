# data.py

raw_esg_data = [
    {
        "CompanyName": "Tesla",
        "Industry": "Tech",
        "Revenue": "360m",
        "EnvironmentData": {
            "GHG Emissions (Scope 1 & 2)": "12,500 tonnes CO2e (Scope 1 & 2)",
            "Renewable Energy Share": "42%",
            "Water Usage Efficiency": "15,000 m³/year",
            "Waste Recycling Rate": "68%",
            "Hazardous Waste": "12 tonnes/year",
            "Environmental Violations": "None",
            "Climate Targets": "25% emission reduction by 2030",
            "EU Taxonomy Alignment": "75%"
        },
        "SocialData": {
            "Workforce Diversity": "34% women, 28% in management",
            "Gender Pay Gap": "7.2%",
            "Health & Safety": "1.8 incidents per 100 employees",
            "Training Hours": "35",
            "Community Investment": "€150,000",
            "Supply Chain Monitoring": "75% audited",
            "Human Rights Policy": "Comprehensive",
            "Product Safety Incidents": "1 minor recall"
        },
        "GovernanceData": {
            "Board Independence": "60%",
            "Board Diversity": "35%",
            "ESG Committee": "Yes",
            "Executive Compensation Linked to ESG": "15%",
            "Anti-corruption Policy": "Yes",
            "Whistleblower System": "Effective",
            "ESG Reporting": "Partial GRI",
            "Tax Transparency": "Country-by-country"
        }
    },
    {
        "CompanyName": "Microsoft",
        "Industry": "Tech",
        "Revenue": "160b",
        "EnvironmentData": {
            "GHG Emissions (Scope 1 & 2)": "10,000 tonnes",
            "Renewable Energy Share": "65%",
            "Water Usage Efficiency": "10,000 m³/year",
            "Waste Recycling Rate": "75%",
            "Hazardous Waste": "5 tonnes/year",
            "Environmental Violations": "None",
            "Climate Targets": "30% reduction by 2030",
            "EU Taxonomy Alignment": "80%"
        },
        "SocialData": {
            "Workforce Diversity": "40% women",
            "Gender Pay Gap": "5%",
            "Health & Safety": "1.0",
            "Training Hours": "40",
            "Community Investment": "€200,000",
            "Supply Chain Monitoring": "80% audited",
            "Human Rights Policy": "Yes",
            "Product Safety Incidents": "None"
        },
        "GovernanceData": {
            "Board Independence": "70%",
            "Board Diversity": "40%",
            "ESG Committee": "Yes",
            "Executive Compensation Linked to ESG": "10%",
            "Anti-corruption Policy": "Yes",
            "Whistleblower System": "Yes",
            "ESG Reporting": "GRI",
            "Tax Transparency": "Yes"
        }
    },
    {
        "CompanyName": "Unilever",
        "Industry": "Consumer Goods",
        "Revenue": "52b",
        "EnvironmentData": {
            "GHG Emissions (Scope 1 & 2)": "9,000 tonnes",
            "Renewable Energy Share": "60%",
            "Water Usage Efficiency": "25,000 m³/year",
            "Waste Recycling Rate": "82%",
            "Hazardous Waste": "3 tonnes/year",
            "Environmental Violations": "None",
            "Climate Targets": "Net zero by 2039",
            "EU Taxonomy Alignment": "60%"
        },
        "SocialData": {
            "Workforce Diversity": "45% women",
            "Gender Pay Gap": "4.5%",
            "Health & Safety": "0.9",
            "Training Hours": "30",
            "Community Investment": "€300,000",
            "Supply Chain Monitoring": "70% audited",
            "Human Rights Policy": "Yes",
            "Product Safety Incidents": "None"
        },
        "GovernanceData": {
            "Board Independence": "65%",
            "Board Diversity": "42%",
            "ESG Committee": "Yes",
            "Executive Compensation Linked to ESG": "20%",
            "Anti-corruption Policy": "Yes",
            "Whistleblower System": "Yes",
            "ESG Reporting": "CDP, GRI",
            "Tax Transparency": "Yes"
        }
    },
    {
        "CompanyName": "Walmart",
        "Industry": "Retail",
        "Revenue": "560b",
        "EnvironmentData": {
            "GHG Emissions (Scope 1 & 2)": "25,000 tonnes",
            "Renewable Energy Share": "35%",
            "Water Usage Efficiency": "100,000 m³/year",
            "Waste Recycling Rate": "55%",
            "Hazardous Waste": "10 tonnes/year",
            "Environmental Violations": "1 minor in 3 years",
            "Climate Targets": "50% reduction by 2040",
            "EU Taxonomy Alignment": "40%"
        },
        "SocialData": {
            "Workforce Diversity": "50% women",
            "Gender Pay Gap": "6%",
            "Health & Safety": "2.2",
            "Training Hours": "25",
            "Community Investment": "€500,000",
            "Supply Chain Monitoring": "60% audited",
            "Human Rights Policy": "Yes",
            "Product Safety Incidents": "2 minor recalls"
        },
        "GovernanceData": {
            "Board Independence": "58%",
            "Board Diversity": "38%",
            "ESG Committee": "Yes",
            "Executive Compensation Linked to ESG": "12%",
            "Anti-corruption Policy": "Yes",
            "Whistleblower System": "Yes",
            "ESG Reporting": "Yes",
            "Tax Transparency": "Yes"
        }
    },
    {
        "CompanyName": "Pfizer",
        "Industry": "Pharmaceuticals",
        "Revenue": "82b",
        "EnvironmentData": {
            "GHG Emissions (Scope 1 & 2)": "5,500 tonnes",
            "Renewable Energy Share": "48%",
            "Water Usage Efficiency": "8,000 m³/year",
            "Waste Recycling Rate": "70%",
            "Hazardous Waste": "15 tonnes/year",
            "Environmental Violations": "None",
            "Climate Targets": "25% reduction by 2030",
            "EU Taxonomy Alignment": "65%"
        },
        "SocialData": {
            "Workforce Diversity": "41% women",
            "Gender Pay Gap": "5.1%",
            "Health & Safety": "1.3",
            "Training Hours": "45",
            "Community Investment": "€250,000",
            "Supply Chain Monitoring": "78% audited",
            "Human Rights Policy": "Yes",
            "Product Safety Incidents": "1"
        },
        "GovernanceData": {
            "Board Independence": "62%",
            "Board Diversity": "40%",
            "ESG Committee": "Yes",
            "Executive Compensation Linked to ESG": "18%",
            "Anti-corruption Policy": "Yes",
            "Whistleblower System": "Yes",
            "ESG Reporting": "GRI, SASB",
            "Tax Transparency": "Yes"
        }
    },
    {
        "CompanyName": "Shell",
        "Industry": "Energy",
        "Revenue": "270b",
        "EnvironmentData": {
            "GHG Emissions (Scope 1 & 2)": "300,000 tonnes",
            "Renewable Energy Share": "20%",
            "Water Usage Efficiency": "200,000 m³/year",
            "Waste Recycling Rate": "35%",
            "Hazardous Waste": "80 tonnes/year",
            "Environmental Violations": "2 in last 5 years",
            "Climate Targets": "Net zero by 2050",
            "EU Taxonomy Alignment": "30%"
        },
        "SocialData": {
            "Workforce Diversity": "30% women",
            "Gender Pay Gap": "9%",
            "Health & Safety": "2.5",
            "Training Hours": "32",
            "Community Investment": "€1,000,000",
            "Supply Chain Monitoring": "55% audited",
            "Human Rights Policy": "Yes",
            "Product Safety Incidents": "3"
        },
        "GovernanceData": {
            "Board Independence": "60%",
            "Board Diversity": "25%",
            "ESG Committee": "Yes",
            "Executive Compensation Linked to ESG": "10%",
            "Anti-corruption Policy": "Yes",
            "Whistleblower System": "Yes",
            "ESG Reporting": "Yes",
            "Tax Transparency": "Partial"
        }
    },
    {
        "CompanyName": "Starbucks",
        "Industry": "Food & Beverage",
        "Revenue": "32b",
        "EnvironmentData": {
            "GHG Emissions (Scope 1 & 2)": "7,500 tonnes",
            "Renewable Energy Share": "78%",
            "Water Usage Efficiency": "50,000 m³/year",
            "Waste Recycling Rate": "80%",
            "Hazardous Waste": "2 tonnes/year",
            "Environmental Violations": "None",
            "Climate Targets": "50% by 2030",
            "EU Taxonomy Alignment": "50%"
        },
        "SocialData": {
            "Workforce Diversity": "55% women",
            "Gender Pay Gap": "3%",
            "Health & Safety": "0.8",
            "Training Hours": "20",
            "Community Investment": "€120,000",
            "Supply Chain Monitoring": "85% audited",
            "Human Rights Policy": "Yes",
            "Product Safety Incidents": "None"
        },
        "GovernanceData": {
            "Board Independence": "75%",
            "Board Diversity": "50%",
            "ESG Committee": "Yes",
            "Executive Compensation Linked to ESG": "10%",
            "Anti-corruption Policy": "Yes",
            "Whistleblower System": "Yes",
            "ESG Reporting": "Full GRI",
            "Tax Transparency": "Yes"
        }
    },
    {
        "CompanyName": "BMW",
        "Industry": "Automotive",
        "Revenue": "110b",
        "EnvironmentData": {
            "GHG Emissions (Scope 1 & 2)": "100,000 tonnes",
            "Renewable Energy Share": "45%",
            "Water Usage Efficiency": "70,000 m³/year",
            "Waste Recycling Rate": "72%",
            "Hazardous Waste": "25 tonnes/year",
            "Environmental Violations": "1 in past 3 years",
            "Climate Targets": "40% reduction by 2035",
            "EU Taxonomy Alignment": "58%"
        },
        "SocialData": {
            "Workforce Diversity": "33% women",
            "Gender Pay Gap": "6%",
            "Health & Safety": "1.5",
            "Training Hours": "36",
            "Community Investment": "€300,000",
            "Supply Chain Monitoring": "60% audited",
            "Human Rights Policy": "Yes",
            "Product Safety Incidents": "1"
        },
        "GovernanceData": {
            "Board Independence": "65%",
            "Board Diversity": "32%",
            "ESG Committee": "Yes",
            "Executive Compensation Linked to ESG": "12%",
            "Anti-corruption Policy": "Yes",
            "Whistleblower System": "Yes",
            "ESG Reporting": "Yes",
            "Tax Transparency": "Yes"
        }
    },
    {
        "CompanyName": "Accenture",
        "Industry": "Consulting",
        "Revenue": "61b",
        "EnvironmentData": {
            "GHG Emissions (Scope 1 & 2)": "4,000 tonnes",
            "Renewable Energy Share": "88%",
            "Water Usage Efficiency": "6,000 m³/year",
            "Waste Recycling Rate": "90%",
            "Hazardous Waste": "1 tonne/year",
            "Environmental Violations": "None",
            "Climate Targets": "Net zero by 2025",
            "EU Taxonomy Alignment": "90%"
        },
        "SocialData": {
            "Workforce Diversity": "48% women",
            "Gender Pay Gap": "2%",
            "Health & Safety": "0.6",
            "Training Hours": "50",
            "Community Investment": "€400,000",
            "Supply Chain Monitoring": "92% audited",
            "Human Rights Policy": "Yes",
            "Product Safety Incidents": "None"
        },
        "GovernanceData": {
            "Board Independence": "70%",
            "Board Diversity": "45%",
            "ESG Committee": "Yes",
            "Executive Compensation Linked to ESG": "15%",
            "Anti-corruption Policy": "Yes",
            "Whistleblower System": "Yes",
            "ESG Reporting": "GRI, CDP",
            "Tax Transparency": "Yes"
        }
    },
    {
        "CompanyName": "Coca-Cola",
        "Industry": "Beverages",
        "Revenue": "46b",
        "EnvironmentData": {
            "GHG Emissions (Scope 1 & 2)": "20,000 tonnes",
            "Renewable Energy Share": "52%",
            "Water Usage Efficiency": "150,000 m³/year",
            "Waste Recycling Rate": "70%",
            "Hazardous Waste": "18 tonnes/year",
            "Environmental Violations": "1 in 5 years",
            "Climate Targets": "30% by 2030",
            "EU Taxonomy Alignment": "45%"
        },
        "SocialData": {
            "Workforce Diversity": "42% women",
            "Gender Pay Gap": "5%",
            "Health & Safety": "1.6",
            "Training Hours": "28",
            "Community Investment": "€180,000",
            "Supply Chain Monitoring": "70% audited",
            "Human Rights Policy": "Yes",
            "Product Safety Incidents": "1 minor"
        },
        "GovernanceData": {
            "Board Independence": "60%",
            "Board Diversity": "38%",
            "ESG Committee": "Yes",
            "Executive Compensation Linked to ESG": "10%",
            "Anti-corruption Policy": "Yes",
            "Whistleblower System": "Yes",
            "ESG Reporting": "Yes",
            "Tax Transparency": "Yes"
        }
    }
]

# Dictionary for fast lookup
ESG_Data = {
    (entry["CompanyName"].lower(), entry["Industry"].lower()): entry
    for entry in raw_esg_data
}
