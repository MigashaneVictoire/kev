# Mitigating the Risk of Known Exploited Vulnerabilities

## Understanding CISA
The Cybersecurity and Infrastructure Security Agency (CISA) serves as the leading authority on cybersecurity vulnerabilities that are actively being exploited. To assist organizations in managing these vulnerabilities and staying up-to-date with evolving threats, CISA advises all entities to regularly review and monitor the Known Exploited Vulnerabilities (KEV) catalog.

## KEV and the KEV Catalog Explained
"KEV" stands for Known Exploited Vulnerabilities, and the KEV Catalog is a critical resource for organizations. It highlights vulnerabilities that are being actively exploited, urging organizations to prioritize their remediation efforts. CISA recommends incorporating the KEV catalog into your organization’s vulnerability management strategy to focus on the most immediate and pressing threats.

## Federal Civilian Executive Branch (FCEB) Agencies
FCEB agencies are part of the U.S. government's executive branch and encompass a range of departments, such as the Department of Homeland Security (DHS), the Department of Health and Human Services (HHS), and the Department of Justice (DOJ), among others. Under Binding Operational Directive (BOD) 22-01, these agencies are required to address vulnerabilities listed in the KEV catalog within specific deadlines. Although BOD 22-01 is not mandatory for state, local, tribal, and territorial (SLTT) governments or private sector organizations, CISA strongly recommends that they also prioritize remediation of these vulnerabilities to enhance their cybersecurity posture.

## Criteria for Including Vulnerabilities in the KEV Catalog

**What is a CVE ID?**

A CVE ID is a unique identifier assigned to a publicly known cybersecurity vulnerability. This is the first criterion for a vulnerability to be considered for inclusion in the KEV catalog.

**Active Exploitation Explained**

Active exploitation refers to the confirmed use of malicious code to take advantage of a vulnerability, with the intent of compromising a system without the owner's consent. In the context of the KEV catalog, vulnerabilities that are actively exploited or have been previously exploited are prioritized for inclusion.

- Exploitable: This term describes how easily an attacker can exploit a vulnerability. Factors such as the availability of a proof-of-concept (PoC), network accessibility, the requirement for privileged access, and the technical skill level needed to carry out the exploit are considered.

**Remediation Actions**

When CISA adds a vulnerability to the KEV catalog, it typically includes clear actions that affected organizations should take. Under BOD 22-01, FCEB agencies are required to:

- Apply security updates as instructed by vendors.
- Remove affected products from agency networks if they have reached end-of-life or cannot be otherwise updated.
CISA also encourages all other organizations to follow these remediation steps to improve their overall security.

## The Goal of the KEV Project

**Binary Classification Model**:

**Goal**: Predict whether a vulnerability is associated with a known ransomware campaign.
- **Approach**: Use features such as `cveID`, `vendorProject`, `product`, `vulnerabilityName`, `shortDescription`, and `dateAdded` to build a binary classification model to classify vulnerabilities as `known` or `unknown` for ransomware campaigns.

- Questions of focus:
    - 1.  Is there a significant association between the vendorProject and the likelihood of a vulnerability being associated with a ransomware campaign?
    - 2. Does the specific vulnerability type significantly influence the classification of a vulnerability as associated with a known ransomware campaign?
    - 3.Question: Does the dateAdded (or the age of the vulnerability) significantly affect the likelihood of being associated with a ransomware campaign?
    - 4. Are certain products more likely to be associated with vulnerabilities targeted by ransomware campaigns?
    - 5. Is there a significant difference in the likelihood of ransomware association among different types of vulnerabilities?

For more impormation, visit the [America's Cyber Defence Agency](https://www.cisa.gov/known-exploited-vulnerabilities)


## Project Outcome and Conclusion:

The KEV project used five models to predict if a vulnerability is linked to a ransomware campaign. The K-Nearest Neighbor (KNN) model performed the best, showing consistent results in both training and validation. However, despite its performance, the improvement in accuracy was minimal (1.8% accuracy improvement). Given the critical nature of the work being done, I do not recommend relying on this model for such high-stakes decision-making.

The project found that things like the vendor, vulnerability type, product, and when the vulnerability was added can help predict if it will be exploited in ransomware attacks. This suggests that CISA's current efforts are working well, but there's still potential to improve how we manage vulnerabilities using data.

**Future Plan**
- Time Series Analysis: Study how the age of vulnerabilities impacts their link to ransomware over time, which could help predict future patterns.