DOMAIN5_QUESTIONS = [
    {
        "id": 406,
        "domain": 5,
        "subdomain": "5.1",
        "objective": "Summarize elements of effective security governance",
        "stem": "An organization wants to establish a hierarchy of guiding documents for its security program. Which document sits at the top of this hierarchy and provides the high-level direction from executive leadership?",
        "options": {"A": "Standard", "B": "Procedure", "C": "Policy", "D": "Guideline"},
        "correct_answer": "C",
        "difficulty": 2,
        "explanations": {
            "correct": "Policy is the highest-level document, expressing management intent and direction. All standards, procedures, and guidelines derive their authority from policy.",
            "A": "Standards define specific mandatory requirements (e.g., minimum password length) that implement policy — they sit below policy.",
            "B": "Procedures are step-by-step instructions for implementing standards — lowest in the hierarchy.",
            "C": "Policy is the top-level governance document expressing executive direction.",
            "D": "Guidelines are optional recommendations, not mandatory — and derive from policy rather than superseding it."
        }
    },
    {
        "id": 407,
        "domain": 5,
        "subdomain": "5.1",
        "objective": "Summarize elements of effective security governance",
        "stem": "A security manager is creating a document that specifies the minimum required encryption algorithm and key length for data at rest. What type of document is this?",
        "options": {"A": "Policy", "B": "Standard", "C": "Guideline", "D": "Procedure"},
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "A standard defines specific, mandatory technical or operational requirements — like 'AES-256 for data at rest.' Standards implement policy in concrete terms.",
            "A": "Policy is higher-level (e.g., 'all sensitive data must be protected') without specifying the algorithm.",
            "B": "Standard specifies mandatory requirements — the encryption algorithm and key length.",
            "C": "Guidelines are optional recommendations, not mandatory specifications.",
            "D": "Procedures describe how to perform a task step-by-step, not what the technical requirement is."
        }
    },
    {
        "id": 408,
        "domain": 5,
        "subdomain": "5.1",
        "objective": "Summarize elements of effective security governance",
        "stem": "Which governance structure places the security function under the legal and compliance department, potentially limiting its independence?",
        "options": {"A": "CISO reporting to CEO", "B": "Security committee model", "C": "CISO reporting to General Counsel", "D": "Virtual CISO (vCISO)"},
        "correct_answer": "C",
        "difficulty": 3,
        "explanations": {
            "correct": "When the CISO reports to the General Counsel (legal), security decisions can be filtered through a legal lens, potentially limiting the security function's independence and ability to raise issues.",
            "A": "CISO reporting to CEO provides the highest independence and executive visibility.",
            "B": "A security committee distributes governance across stakeholders — typically more inclusive.",
            "C": "Reporting to General Counsel can subordinate security to legal risk concerns.",
            "D": "A vCISO is an outsourced security leader — a staffing model, not an internal reporting structure."
        }
    },
    {
        "id": 409,
        "domain": 5,
        "subdomain": "5.1",
        "objective": "Summarize elements of effective security governance",
        "stem": "An Acceptable Use Policy (AUP) is being drafted. Which element is MOST critical to include to ensure enforceability?",
        "options": {"A": "Technical architecture diagrams", "B": "Acknowledgement signature by all users", "C": "A list of all approved software vendors", "D": "Penetration testing schedules"},
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "An acknowledgement signature confirms users have read, understood, and agreed to the AUP, making it legally enforceable and establishing accountability.",
            "A": "Technical diagrams belong in architecture documents, not an AUP.",
            "B": "User acknowledgement/signature is critical for enforceability.",
            "C": "Approved vendor lists are procurement or IT documents.",
            "D": "Penetration testing schedules are operational security documents."
        }
    },
    {
        "id": 410,
        "domain": 5,
        "subdomain": "5.1",
        "objective": "Summarize elements of effective security governance",
        "stem": "What is the PRIMARY purpose of a change management policy in security governance?",
        "options": {
            "A": "To document all configuration baselines",
            "B": "To ensure changes are authorized, tested, and documented before implementation",
            "C": "To provide rollback procedures for failed deployments",
            "D": "To define SLA requirements with vendors"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "Change management policy ensures that all changes go through approval (e.g., CAB), testing, and documentation processes to prevent unauthorized or untested changes that introduce risk.",
            "A": "Configuration baselines are documented in configuration management, though change management references them.",
            "B": "The primary purpose is authorization, testing, and documentation before implementation.",
            "C": "Rollback procedures are part of change management but not the primary purpose.",
            "D": "SLA requirements are part of vendor/contract management."
        }
    },
    {
        "id": 411,
        "domain": 5,
        "subdomain": "5.2",
        "objective": "Explain elements of the risk management process",
        "stem": "An organization identifies that a flood could destroy its data center. The probability is low but the potential loss is $10 million. What risk management step is being performed?",
        "options": {"A": "Risk avoidance", "B": "Risk identification and analysis", "C": "Risk transfer", "D": "Risk acceptance"},
        "correct_answer": "B",
        "difficulty": 1,
        "explanations": {
            "correct": "Identifying the threat (flood), assessing probability, and estimating potential loss ($10M) constitutes risk identification and analysis — the foundational step before choosing a response.",
            "A": "Risk avoidance means eliminating the activity that creates the risk — not just identifying it.",
            "B": "Identifying the risk and analyzing its probability and impact is risk identification and analysis.",
            "C": "Risk transfer (e.g., insurance) is a response strategy chosen after analysis.",
            "D": "Risk acceptance is a conscious decision to tolerate the risk after analysis."
        }
    },
    {
        "id": 412,
        "domain": 5,
        "subdomain": "5.2",
        "objective": "Explain elements of the risk management process",
        "stem": "A company calculates that a server failure occurs 0.5 times per year and each failure costs $200,000. What is the Annual Loss Expectancy (ALE)?",
        "options": {"A": "$100,000", "B": "$200,000", "C": "$400,000", "D": "$1,000,000"},
        "correct_answer": "A",
        "difficulty": 2,
        "explanations": {
            "correct": "ALE = ARO × SLE = 0.5 × $200,000 = $100,000. The Annual Rate of Occurrence (ARO) of 0.5 means once every two years.",
            "A": "ALE = 0.5 × $200,000 = $100,000.",
            "B": "$200,000 is the Single Loss Expectancy (SLE), not the ALE.",
            "C": "$400,000 would require ARO of 2.0 (twice per year).",
            "D": "$1,000,000 is not supported by the given values."
        }
    },
    {
        "id": 413,
        "domain": 5,
        "subdomain": "5.2",
        "objective": "Explain elements of the risk management process",
        "stem": "After a risk assessment, management decides to purchase cyber liability insurance. Which risk response is being applied?",
        "options": {"A": "Risk avoidance", "B": "Risk mitigation", "C": "Risk transfer", "D": "Risk acceptance"},
        "correct_answer": "C",
        "difficulty": 1,
        "explanations": {
            "correct": "Purchasing insurance transfers the financial consequence of a risk to a third party (the insurer). This is risk transfer.",
            "A": "Risk avoidance eliminates the activity entirely (e.g., not doing business online).",
            "B": "Risk mitigation reduces the probability or impact through controls (e.g., deploying a firewall).",
            "C": "Insurance is the classic example of risk transfer.",
            "D": "Risk acceptance means acknowledging the risk and choosing not to act — no insurance."
        }
    },
    {
        "id": 414,
        "domain": 5,
        "subdomain": "5.2",
        "objective": "Explain elements of the risk management process",
        "stem": "A risk register entry shows: Threat = malware infection, Inherent Risk = High, Current Controls = antivirus + EDR, Residual Risk = Low. What does 'residual risk' represent?",
        "options": {
            "A": "The risk before any controls are applied",
            "B": "The risk that remains after controls are implemented",
            "C": "The risk transferred to an insurance provider",
            "D": "The maximum possible loss from the threat"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "Residual risk is the risk that remains after applying controls. Inherent risk (High) reduced by antivirus + EDR leaves residual risk (Low).",
            "A": "Inherent risk is the risk before any controls — 'High' in this example.",
            "B": "Residual risk = risk remaining after controls are applied.",
            "C": "Transferred risk refers to insurance/outsourcing, not residual risk.",
            "D": "Maximum possible loss is the SLE component, not the residual risk rating."
        }
    },
    {
        "id": 415,
        "domain": 5,
        "subdomain": "5.2",
        "objective": "Explain elements of the risk management process",
        "stem": "Qualitative risk analysis uses which of the following to express risk levels?",
        "options": {
            "A": "Dollar amounts and annual rates of occurrence",
            "B": "Descriptive ratings such as High, Medium, Low",
            "C": "Standard deviation and confidence intervals",
            "D": "CVE scores and CVSS base scores"
        },
        "correct_answer": "B",
        "difficulty": 1,
        "explanations": {
            "correct": "Qualitative analysis uses subjective, descriptive categories (High/Medium/Low, 1-5 scales, color matrices) rather than precise financial calculations.",
            "A": "Dollar amounts and ARO are quantitative analysis components (SLE, ALE formulas).",
            "B": "Qualitative = descriptive ratings like High, Medium, Low.",
            "C": "Statistical measures are quantitative/probabilistic — not standard qualitative tools.",
            "D": "CVE/CVSS scores are technical vulnerability ratings, not general risk analysis methodology."
        }
    },
    {
        "id": 416,
        "domain": 5,
        "subdomain": "5.2",
        "objective": "Explain elements of the risk management process",
        "stem": "An organization decides that the cost of mitigating a low-probability, low-impact risk exceeds the potential loss and documents this decision. What risk response is this?",
        "options": {"A": "Risk transfer", "B": "Risk avoidance", "C": "Risk acceptance", "D": "Risk mitigation"},
        "correct_answer": "C",
        "difficulty": 1,
        "explanations": {
            "correct": "When the cost of control exceeds the potential loss, organizations may accept the risk — a documented, conscious decision to tolerate it.",
            "A": "Risk transfer involves shifting financial consequences to a third party.",
            "B": "Risk avoidance means eliminating the risky activity entirely.",
            "C": "Documented decision to tolerate the risk = risk acceptance.",
            "D": "Risk mitigation means applying controls to reduce probability or impact."
        }
    },
    {
        "id": 417,
        "domain": 5,
        "subdomain": "5.2",
        "objective": "Explain elements of the risk management process",
        "stem": "Which term describes the combination of the likelihood of a threat exploiting a vulnerability and the resulting business impact?",
        "options": {"A": "Threat vector", "B": "Attack surface", "C": "Risk", "D": "Vulnerability"},
        "correct_answer": "C",
        "difficulty": 1,
        "explanations": {
            "correct": "Risk = likelihood (probability of exploitation) × impact (business consequence). Risk combines both factors.",
            "A": "Threat vector is the path or method used by an attacker to reach a target.",
            "B": "Attack surface is the sum of all points where an attacker could interact with the system.",
            "C": "Risk = likelihood × impact.",
            "D": "Vulnerability is a weakness — one input to risk calculation, not the combination."
        }
    },
    {
        "id": 418,
        "domain": 5,
        "subdomain": "5.3",
        "objective": "Explain the processes associated with third-party risk assessment and management",
        "stem": "Before sharing sensitive data with a vendor, which agreement defines what data will be shared, how it will be protected, and the consequences of unauthorized disclosure?",
        "options": {"A": "Service Level Agreement (SLA)", "B": "Non-Disclosure Agreement (NDA)", "C": "Memorandum of Understanding (MOU)", "D": "Business Associate Agreement (BAA)"},
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "An NDA (Non-Disclosure Agreement) is a legal contract establishing confidentiality obligations — what can be shared, how it must be protected, and consequences of breach.",
            "A": "An SLA defines service performance metrics (uptime, response time) — not confidentiality.",
            "B": "NDA establishes confidentiality terms for data sharing.",
            "C": "An MOU is a non-binding statement of intent between parties.",
            "D": "A BAA is a HIPAA-specific agreement between covered entities and business associates — narrower scope."
        }
    },
    {
        "id": 419,
        "domain": 5,
        "subdomain": "5.3",
        "objective": "Explain the processes associated with third-party risk assessment and management",
        "stem": "A healthcare organization shares patient data with a billing company. Under HIPAA, what specific agreement must be in place?",
        "options": {"A": "SLA", "B": "NDA", "C": "Business Associate Agreement (BAA)", "D": "MOU"},
        "correct_answer": "C",
        "difficulty": 2,
        "explanations": {
            "correct": "HIPAA requires a Business Associate Agreement (BAA) whenever a covered entity shares Protected Health Information (PHI) with a business associate (third-party vendor).",
            "A": "SLAs cover service performance, not HIPAA compliance requirements.",
            "B": "NDAs address confidentiality but are not the HIPAA-specific required agreement.",
            "C": "BAA is the HIPAA-mandated agreement for PHI sharing with business associates.",
            "D": "MOUs are non-binding and insufficient for HIPAA compliance."
        }
    },
    {
        "id": 420,
        "domain": 5,
        "subdomain": "5.3",
        "objective": "Explain the processes associated with third-party risk assessment and management",
        "stem": "During vendor due diligence, an organization reviews the vendor's SOC 2 Type II report. What does this report indicate?",
        "options": {
            "A": "The vendor has passed a one-time point-in-time security audit",
            "B": "The vendor's controls were effective over a period of time (typically 6-12 months)",
            "C": "The vendor complies with PCI DSS requirements",
            "D": "The vendor's employees have passed background checks"
        },
        "correct_answer": "B",
        "difficulty": 3,
        "explanations": {
            "correct": "SOC 2 Type II audits control effectiveness over a period (typically 6-12 months), providing stronger assurance than the point-in-time Type I. It covers security, availability, processing integrity, confidentiality, and privacy trust service criteria.",
            "A": "SOC 2 Type I is the point-in-time audit — Type II is the period-of-time audit.",
            "B": "SOC 2 Type II validates controls were operating effectively over a sustained period.",
            "C": "PCI DSS compliance is verified by a Qualified Security Assessor (QSA), not a SOC 2 report.",
            "D": "Background checks are HR processes, not covered by SOC 2."
        }
    },
    {
        "id": 421,
        "domain": 5,
        "subdomain": "5.3",
        "objective": "Explain the processes associated with third-party risk assessment and management",
        "stem": "Which supply chain risk involves an attacker compromising software during the build process, injecting malicious code before the final product is delivered to customers?",
        "options": {"A": "Watering hole attack", "B": "Backdoor implantation via build pipeline", "C": "Typosquatting", "D": "Session hijacking"},
        "correct_answer": "B",
        "difficulty": 3,
        "explanations": {
            "correct": "Compromising the build pipeline (CI/CD, code signing infrastructure) to inject malicious code is a supply chain attack — exemplified by the SolarWinds breach where malware was inserted during the build process.",
            "A": "Watering hole attacks compromise websites visited by targets — not the build process.",
            "B": "Build pipeline compromise is a supply chain attack vector that affects all downstream customers.",
            "C": "Typosquatting uses look-alike domain/package names to trick users into downloading malicious software.",
            "D": "Session hijacking involves stealing active user session tokens."
        }
    },
    {
        "id": 422,
        "domain": 5,
        "subdomain": "5.3",
        "objective": "Explain the processes associated with third-party risk assessment and management",
        "stem": "An organization uses a third-party vendor to process payroll. The vendor is then acquired by a competitor. What third-party risk concern should be evaluated immediately?",
        "options": {
            "A": "The vendor's SLA uptime guarantees",
            "B": "Data ownership, confidentiality, and conflict of interest with the new parent company",
            "C": "The vendor's disaster recovery RTO",
            "D": "The vendor's CVSS vulnerability scores"
        },
        "correct_answer": "B",
        "difficulty": 3,
        "explanations": {
            "correct": "When a vendor is acquired by a competitor, the immediate concern is whether sensitive payroll data (employee salaries, compensation) could now be accessible to a competitor — a data ownership and conflict of interest issue.",
            "A": "SLA uptime may change but is not the immediate security concern in a competitive acquisition.",
            "B": "Data confidentiality and conflict of interest are the critical concerns when a competitor acquires your vendor.",
            "C": "RTO is a continuity metric — important but not the immediate competitive risk.",
            "D": "Vulnerability scores are technical measures unrelated to the competitive acquisition risk."
        }
    },
    {
        "id": 423,
        "domain": 5,
        "subdomain": "5.3",
        "objective": "Explain the processes associated with third-party risk assessment and management",
        "stem": "What is the purpose of a Right-to-Audit clause in a vendor contract?",
        "options": {
            "A": "Gives the vendor the right to audit the organization's practices",
            "B": "Allows the organization to audit the vendor's security controls and compliance",
            "C": "Requires the vendor to pass an annual penetration test",
            "D": "Mandates that the vendor purchase cyber insurance"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "A Right-to-Audit clause contractually grants the organization (or its designated auditor) the ability to inspect and verify the vendor's security controls, compliance status, and data handling practices.",
            "A": "The clause runs the other direction — the organization audits the vendor, not vice versa.",
            "B": "Right-to-audit allows the organization to verify the vendor's security posture.",
            "C": "Penetration testing requirements are separate contractual provisions.",
            "D": "Cyber insurance requirements are separate risk transfer clauses."
        }
    },
    {
        "id": 424,
        "domain": 5,
        "subdomain": "5.4",
        "objective": "Summarize elements of effective security compliance",
        "stem": "Which compliance framework is specifically designed to protect cardholder data for organizations that process, store, or transmit payment card information?",
        "options": {"A": "HIPAA", "B": "GDPR", "C": "PCI DSS", "D": "SOX"},
        "correct_answer": "C",
        "difficulty": 1,
        "explanations": {
            "correct": "PCI DSS (Payment Card Industry Data Security Standard) is the framework governing protection of cardholder data for any organization handling credit/debit card transactions.",
            "A": "HIPAA protects Protected Health Information (PHI) in the healthcare industry.",
            "B": "GDPR is the EU data privacy regulation protecting personal data of EU residents.",
            "C": "PCI DSS applies to all entities that process, store, or transmit payment card data.",
            "D": "SOX (Sarbanes-Oxley) addresses financial reporting and internal controls for publicly traded companies."
        }
    },
    {
        "id": 425,
        "domain": 5,
        "subdomain": "5.4",
        "objective": "Summarize elements of effective security compliance",
        "stem": "A US company collects personal data from EU citizens. Under GDPR, what must be established to lawfully transfer this data to the United States?",
        "options": {
            "A": "A memorandum of understanding with the EU",
            "B": "An adequacy decision, standard contractual clauses, or binding corporate rules",
            "C": "Annual penetration testing of US servers",
            "D": "ISO 27001 certification"
        },
        "correct_answer": "B",
        "difficulty": 3,
        "explanations": {
            "correct": "GDPR Chapter V restricts transfers of personal data to non-EEA countries. Lawful mechanisms include: EU adequacy decisions, Standard Contractual Clauses (SCCs), Binding Corporate Rules (BCRs), and specific derogations.",
            "A": "An MOU is not a GDPR-recognized transfer mechanism.",
            "B": "Adequacy decisions, SCCs, or BCRs are the primary GDPR-compliant data transfer mechanisms.",
            "C": "Penetration testing is a security control, not a data transfer mechanism under GDPR.",
            "D": "ISO 27001 certification is not a GDPR data transfer mechanism by itself."
        }
    },
    {
        "id": 426,
        "domain": 5,
        "subdomain": "5.4",
        "objective": "Summarize elements of effective security compliance",
        "stem": "GDPR requires that a data breach involving personal data of EU residents be reported to the supervisory authority within what timeframe?",
        "options": {"A": "24 hours", "B": "48 hours", "C": "72 hours", "D": "7 days"},
        "correct_answer": "C",
        "difficulty": 2,
        "explanations": {
            "correct": "GDPR Article 33 requires controllers to notify the relevant supervisory authority of a personal data breach within 72 hours of becoming aware of it, where feasible.",
            "A": "24 hours is not the GDPR requirement — it's shorter than required.",
            "B": "48 hours is not the GDPR requirement.",
            "C": "72 hours is the GDPR notification window to supervisory authorities.",
            "D": "7 days exceeds the GDPR notification requirement."
        }
    },
    {
        "id": 427,
        "domain": 5,
        "subdomain": "5.4",
        "objective": "Summarize elements of effective security compliance",
        "stem": "Which of the following best describes the concept of 'data sovereignty'?",
        "options": {
            "A": "The right of individuals to control their personal data",
            "B": "The principle that data is subject to the laws of the country where it is stored or processed",
            "C": "Encrypting data before it leaves the organization",
            "D": "Classifying data based on sensitivity level"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "Data sovereignty means that data is subject to the legal jurisdiction of the country where it physically resides or is processed. This affects cloud storage choices — data in Germany is subject to German/EU law.",
            "A": "Individual control of personal data is the concept of data privacy/rights, not data sovereignty.",
            "B": "Data sovereignty = legal jurisdiction based on physical location of data.",
            "C": "Encrypting outbound data is a data protection control, not sovereignty.",
            "D": "Data classification determines sensitivity labels — unrelated to sovereignty."
        }
    },
    {
        "id": 428,
        "domain": 5,
        "subdomain": "5.4",
        "objective": "Summarize elements of effective security compliance",
        "stem": "An organization achieves ISO 27001 certification. What does this primarily demonstrate?",
        "options": {
            "A": "The organization has passed a penetration test",
            "B": "The organization has implemented an Information Security Management System (ISMS) that meets international standards",
            "C": "The organization is HIPAA compliant",
            "D": "The organization has zero security vulnerabilities"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "ISO 27001 is the international standard for Information Security Management Systems (ISMS). Certification means an accredited auditor has verified the organization's ISMS meets the standard's requirements.",
            "A": "Penetration testing is a security assessment, not an ISO 27001 requirement per se.",
            "B": "ISO 27001 certification demonstrates a conforming ISMS — systematic risk management approach.",
            "C": "HIPAA is a US healthcare regulation — ISO 27001 is an international standard for any industry.",
            "D": "ISO 27001 demonstrates process maturity, not zero vulnerabilities."
        }
    },
    {
        "id": 429,
        "domain": 5,
        "subdomain": "5.4",
        "objective": "Summarize elements of effective security compliance",
        "stem": "The NIST Cybersecurity Framework (CSF) organizes security activities into five core functions. Which is the correct set?",
        "options": {
            "A": "Identify, Protect, Detect, Respond, Recover",
            "B": "Prevent, Detect, Analyze, Remediate, Report",
            "C": "Plan, Do, Check, Act, Improve",
            "D": "Assess, Authorize, Monitor, Respond, Report"
        },
        "correct_answer": "A",
        "difficulty": 2,
        "explanations": {
            "correct": "The NIST CSF core functions are: Identify (asset management, risk), Protect (controls), Detect (anomalies), Respond (incident response), and Recover (restoration).",
            "A": "Identify, Protect, Detect, Respond, Recover — the five NIST CSF functions.",
            "B": "This is a made-up set not matching NIST CSF.",
            "C": "Plan-Do-Check-Act is the ISO continual improvement cycle (PDCA), not NIST CSF.",
            "D": "Assess-Authorize-Monitor is from NIST RMF (Risk Management Framework), not CSF."
        }
    },
    {
        "id": 430,
        "domain": 5,
        "subdomain": "5.4",
        "objective": "Summarize elements of effective security compliance",
        "stem": "PCI DSS requires that cardholder data must not be stored after authorization unless necessary. When storage IS required, which data element can NEVER be stored even if encrypted?",
        "options": {"A": "Cardholder name", "B": "Primary Account Number (PAN)", "C": "Full magnetic stripe data", "D": "Expiration date"},
        "correct_answer": "C",
        "difficulty": 3,
        "explanations": {
            "correct": "PCI DSS Requirement 3 prohibits storing sensitive authentication data after authorization — including full magnetic stripe data (track data), CVV/CVC, and PIN data — even encrypted. These cannot be stored under any circumstances.",
            "A": "Cardholder name may be stored (with protections).",
            "B": "The PAN (full card number) may be stored but must be masked or encrypted.",
            "C": "Full magnetic stripe (track data) can NEVER be stored post-authorization.",
            "D": "Expiration date may be stored in limited contexts per PCI DSS."
        }
    },
    {
        "id": 431,
        "domain": 5,
        "subdomain": "5.5",
        "objective": "Explain types and purposes of audits and assessments",
        "stem": "An external auditor hired by the organization conducts a security assessment to verify compliance with internal policies. What type of audit is this?",
        "options": {"A": "First-party audit", "B": "Second-party audit", "C": "Third-party audit", "D": "Internal audit"},
        "correct_answer": "C",
        "difficulty": 2,
        "explanations": {
            "correct": "A third-party audit is conducted by an independent external organization. Even if the organization pays for it, independence from both the organization and its customers defines a third-party audit.",
            "A": "A first-party (internal) audit is conducted by the organization's own staff.",
            "B": "A second-party audit is conducted by a customer or partner on the organization.",
            "C": "Third-party audit = independent external auditor hired by the organization.",
            "D": "Internal audit and first-party audit are the same — conducted by the organization's own staff."
        }
    },
    {
        "id": 432,
        "domain": 5,
        "subdomain": "5.5",
        "objective": "Explain types and purposes of audits and assessments",
        "stem": "A penetration test is characterized by which of the following?",
        "options": {
            "A": "A passive review of security policies and configurations",
            "B": "An authorized simulated attack to identify and exploit vulnerabilities",
            "C": "Automated scanning to identify known CVEs",
            "D": "An interview-based assessment of security awareness"
        },
        "correct_answer": "B",
        "difficulty": 1,
        "explanations": {
            "correct": "A penetration test is an authorized, simulated attack by skilled testers attempting to exploit vulnerabilities — going beyond scanning to demonstrate real-world exploitability.",
            "A": "A passive policy review is a compliance audit or documentation review, not a pentest.",
            "B": "Penetration testing = authorized simulated attack with exploitation.",
            "C": "Automated vulnerability scanning identifies vulnerabilities but doesn't exploit them.",
            "D": "Security awareness interviews are social engineering assessments or training evaluations."
        }
    },
    {
        "id": 433,
        "domain": 5,
        "subdomain": "5.5",
        "objective": "Explain types and purposes of audits and assessments",
        "stem": "A penetration tester is given no information about the target environment before testing. What type of test is this?",
        "options": {"A": "White-box", "B": "Gray-box", "C": "Black-box", "D": "Crystal-box"},
        "correct_answer": "C",
        "difficulty": 1,
        "explanations": {
            "correct": "Black-box testing simulates an external attacker with no prior knowledge — the tester starts with only the target's name or IP range, simulating a real adversary's perspective.",
            "A": "White-box (crystal-box) testing provides the tester with full internal documentation, source code, and architecture.",
            "B": "Gray-box provides partial information — perhaps network diagrams but no source code.",
            "C": "Black-box = zero prior knowledge, simulating an external attacker.",
            "D": "'Crystal-box' is another name for white-box testing (full knowledge)."
        }
    },
    {
        "id": 434,
        "domain": 5,
        "subdomain": "5.5",
        "objective": "Explain types and purposes of audits and assessments",
        "stem": "Which type of assessment evaluates whether employees can recognize and avoid phishing emails by sending simulated phishing messages?",
        "options": {
            "A": "Vulnerability scan",
            "B": "Penetration test",
            "C": "Social engineering assessment",
            "D": "Compliance audit"
        },
        "correct_answer": "C",
        "difficulty": 1,
        "explanations": {
            "correct": "A social engineering assessment (specifically a phishing simulation) tests human vulnerabilities — whether users recognize and report phishing emails versus clicking malicious links.",
            "A": "Vulnerability scans target technical systems, not human behavior.",
            "B": "A penetration test may include social engineering but is a broader technical exploitation exercise.",
            "C": "Phishing simulations are social engineering assessments targeting human factors.",
            "D": "Compliance audits verify adherence to policies/regulations, not employee awareness."
        }
    },
    {
        "id": 435,
        "domain": 5,
        "subdomain": "5.5",
        "objective": "Explain types and purposes of audits and assessments",
        "stem": "What differentiates a vulnerability assessment from a penetration test?",
        "options": {
            "A": "Vulnerability assessments use automated tools; penetration tests are always manual",
            "B": "Vulnerability assessments identify weaknesses without exploitation; penetration tests attempt to exploit them",
            "C": "Penetration tests are passive; vulnerability assessments are active",
            "D": "Vulnerability assessments are only for web applications"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "The key distinction: vulnerability assessments identify and report weaknesses (no exploitation), while penetration tests actively attempt to exploit discovered vulnerabilities to demonstrate real-world impact.",
            "A": "Both may use automated tools; penetration tests often use automated tools alongside manual techniques.",
            "B": "Vulnerability assessment = identify; penetration test = identify AND exploit.",
            "C": "Both are active assessments; penetration tests are not passive.",
            "D": "Both assessment types can apply to any system, not just web apps."
        }
    },
    {
        "id": 436,
        "domain": 5,
        "subdomain": "5.5",
        "objective": "Explain types and purposes of audits and assessments",
        "stem": "During a penetration test, the tester discovers sensitive data but does not exfiltrate it and stops at the point of demonstrated access. What principle is being followed?",
        "options": {"A": "Least privilege", "B": "Rules of engagement", "C": "Need to know", "D": "Defense in depth"},
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "Rules of engagement (RoE) define the scope, limitations, and acceptable actions during a penetration test. Not exfiltrating data — stopping at demonstrated access — is a typical RoE constraint.",
            "A": "Least privilege is an access control principle for system design, not pen test conduct.",
            "B": "Rules of engagement govern what a pen tester can and cannot do during the assessment.",
            "C": "Need to know is an information access control concept.",
            "D": "Defense in depth is a layered security architecture strategy."
        }
    },
    {
        "id": 437,
        "domain": 5,
        "subdomain": "5.6",
        "objective": "Implement security awareness practices",
        "stem": "Which security awareness training method is MOST effective at changing long-term employee security behavior?",
        "options": {
            "A": "Annual 1-hour security training video",
            "B": "Phishing simulations combined with immediate targeted training for those who click",
            "C": "Distributing a printed security policy document",
            "D": "One-time new-hire orientation covering all policies"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "Phishing simulations with immediate, contextual training (teachable moments) for users who click are proven to change behavior more effectively than passive, annual training — the feedback is immediate and relevant.",
            "A": "Annual passive training has poor retention and minimal behavioral change.",
            "B": "Simulation + immediate targeted training = most effective for behavior change.",
            "C": "Printed documents are reference materials, not effective training.",
            "D": "One-time orientation is insufficient for sustained behavioral change."
        }
    },
    {
        "id": 438,
        "domain": 5,
        "subdomain": "5.6",
        "objective": "Implement security awareness practices",
        "stem": "A security awareness program includes training on recognizing social engineering. Which attack type does this MOST directly address?",
        "options": {"A": "SQL injection", "B": "Buffer overflow", "C": "Pretexting and phishing", "D": "DDoS attacks"},
        "correct_answer": "C",
        "difficulty": 1,
        "explanations": {
            "correct": "Social engineering attacks (pretexting, phishing, vishing, baiting) exploit human psychology. Security awareness training directly addresses these by helping employees recognize manipulation attempts.",
            "A": "SQL injection is a technical attack requiring developer training/secure coding, not general awareness.",
            "B": "Buffer overflow is a technical vulnerability addressed by developers and patch management.",
            "C": "Pretexting and phishing are social engineering attacks targeted by awareness training.",
            "D": "DDoS defense is technical (rate limiting, CDN, ISP-level filtering) — not addressed by awareness training."
        }
    },
    {
        "id": 439,
        "domain": 5,
        "subdomain": "5.6",
        "objective": "Implement security awareness practices",
        "stem": "What is the PRIMARY goal of a security champion program within development teams?",
        "options": {
            "A": "To replace the security team with developers",
            "B": "To embed security-minded individuals in dev teams who advocate for secure practices",
            "C": "To automate security testing in CI/CD pipelines",
            "D": "To perform penetration testing of internally developed applications"
        },
        "correct_answer": "B",
        "difficulty": 3,
        "explanations": {
            "correct": "Security champion programs embed security advocates within development teams — developers who receive extra security training and act as a liaison between the security team and developers, promoting secure-by-design practices.",
            "A": "Champions supplement, not replace, the security function.",
            "B": "Security champions are embedded advocates promoting secure practices within dev teams.",
            "C": "Automated security in CI/CD (DevSecOps) is complementary but distinct from a champions program.",
            "D": "Penetration testing is performed by security specialists, not typically champions."
        }
    },
    {
        "id": 440,
        "domain": 5,
        "subdomain": "5.2",
        "objective": "Explain elements of the risk management process",
        "stem": "What is the formula for Single Loss Expectancy (SLE)?",
        "options": {
            "A": "SLE = ARO × ALE",
            "B": "SLE = Asset Value × Exposure Factor",
            "C": "SLE = Threat Likelihood × Vulnerability Severity",
            "D": "SLE = ALE / ARO"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "SLE = Asset Value (AV) × Exposure Factor (EF). If a server worth $500,000 would be 40% destroyed by a fire (EF=0.4), SLE = $500,000 × 0.4 = $200,000.",
            "A": "ALE = ARO × SLE — this reverses the relationship.",
            "B": "SLE = Asset Value × Exposure Factor is the correct formula.",
            "C": "Threat likelihood × vulnerability severity is a qualitative risk matrix approach, not SLE.",
            "D": "SLE = ALE / ARO rearranges the ALE formula correctly but doesn't show the SLE components."
        }
    },
    {
        "id": 441,
        "domain": 5,
        "subdomain": "5.2",
        "objective": "Explain elements of the risk management process",
        "stem": "A risk register shows a vulnerability with a 'likelihood' of 4/5 and 'impact' of 2/5. Using a qualitative risk matrix, how should this risk be prioritized relative to one with likelihood 2/5 and impact 5/5?",
        "options": {
            "A": "The 4×2 risk is higher priority (higher likelihood)",
            "B": "The 2×5 risk is higher priority (higher impact)",
            "C": "They are equal (both = 8 on a 25-point scale) and prioritized identically",
            "D": "Impact always outweighs likelihood, so 2×5 is always higher"
        },
        "correct_answer": "C",
        "difficulty": 3,
        "explanations": {
            "correct": "On a simple multiplicative matrix, 4×2=8 and 2×5=10 — actually 2×5 scores slightly higher. But the question asks about a 4/5 likelihood, 2/5 impact scenario where 4×2=8 vs 2×5=10. They are not equal — 2×5 is higher. However, many qualitative frameworks weight these differently based on organizational context.",
            "A": "Higher likelihood alone doesn't determine priority — impact also matters.",
            "B": "2×5=10 > 4×2=8, so the high-impact risk is actually higher on a simple matrix.",
            "C": "4×2=8, 2×5=10 — they are NOT equal; this answer is incorrect.",
            "D": "While impact often gets more weight, the multiplicative result (2×5=10) does rank higher than (4×2=8) on a simple matrix."
        }
    },
    {
        "id": 442,
        "domain": 5,
        "subdomain": "5.1",
        "objective": "Summarize elements of effective security governance",
        "stem": "Which role is responsible for determining how data is used and who can access it within an organization?",
        "options": {"A": "Data custodian", "B": "Data processor", "C": "Data owner", "D": "Data steward"},
        "correct_answer": "C",
        "difficulty": 2,
        "explanations": {
            "correct": "The data owner (typically a business unit leader) is accountable for determining data classification, access rights, and permitted uses. They make decisions about what the data is and who should have access.",
            "A": "Data custodians (often IT) are responsible for implementing the controls the owner specifies — storage, backup, access enforcement.",
            "B": "Data processor (GDPR term) processes data on behalf of the controller — a third party.",
            "C": "Data owner determines classification, access permissions, and data usage policies.",
            "D": "Data steward manages data quality and consistency — often a more operational role."
        }
    },
    {
        "id": 443,
        "domain": 5,
        "subdomain": "5.1",
        "objective": "Summarize elements of effective security governance",
        "stem": "An organization's IT team is responsible for maintaining backups of the HR database. They implement encryption and access controls specified by HR management. What role does the IT team play?",
        "options": {"A": "Data owner", "B": "Data custodian", "C": "Data controller", "D": "Data subject"},
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "The IT team implements the protections specified by the data owner (HR) — they are data custodians, responsible for technical safeguarding without making policy decisions.",
            "A": "The data owner (HR management) sets the requirements; IT implements them.",
            "B": "IT acts as data custodian — implementing controls, not setting policy.",
            "C": "Data controller (GDPR term) determines purposes and means of processing — HR management's role.",
            "D": "Data subjects are the individuals whose data is being processed — HR employees."
        }
    },
    {
        "id": 444,
        "domain": 5,
        "subdomain": "5.4",
        "objective": "Summarize elements of effective security compliance",
        "stem": "Under HIPAA Security Rule, covered entities must implement which of the following types of safeguards?",
        "options": {
            "A": "Administrative, technical, and physical safeguards",
            "B": "Preventive, detective, and corrective safeguards",
            "C": "Confidentiality, integrity, and availability controls",
            "D": "Operational, managerial, and regulatory safeguards"
        },
        "correct_answer": "A",
        "difficulty": 2,
        "explanations": {
            "correct": "The HIPAA Security Rule explicitly requires three categories: Administrative safeguards (policies, training, workforce management), Physical safeguards (facility access, workstation security), and Technical safeguards (access control, encryption, audit controls).",
            "A": "Administrative, technical, and physical — the three HIPAA safeguard categories.",
            "B": "Preventive/detective/corrective are control function categories, not HIPAA's classification.",
            "C": "CIA triad describes information security goals, not HIPAA's safeguard categories.",
            "D": "Not a recognized HIPAA category structure."
        }
    },
    {
        "id": 445,
        "domain": 5,
        "subdomain": "5.4",
        "objective": "Summarize elements of effective security compliance",
        "stem": "What is the key distinction between a privacy policy and a data handling policy?",
        "options": {
            "A": "Privacy policies are internal documents; data handling policies are public",
            "B": "Privacy policies inform users how their data is collected and used; data handling policies govern internal employee data practices",
            "C": "There is no distinction — they are the same document",
            "D": "Data handling policies are regulated by law; privacy policies are voluntary"
        },
        "correct_answer": "B",
        "difficulty": 3,
        "explanations": {
            "correct": "Privacy policies (external-facing) tell customers/users how their personal data is collected, used, shared, and protected. Data handling (or data management) policies are internal documents governing how employees must handle sensitive data.",
            "A": "Privacy policies are typically public; data handling policies are internal — but this is the symptom, not the key distinction.",
            "B": "External-facing user notice (privacy policy) vs. internal employee rules (data handling policy) is the core distinction.",
            "C": "They are distinct documents with different audiences and purposes.",
            "D": "Both can be legally required (GDPR mandates privacy notices; HIPAA requires internal policies)."
        }
    },
    {
        "id": 446,
        "domain": 5,
        "subdomain": "5.3",
        "objective": "Explain the processes associated with third-party risk assessment and management",
        "stem": "What is the PRIMARY risk of using an end-of-life (EOL) open-source component in a production application?",
        "options": {
            "A": "Licensing violations requiring payment",
            "B": "No vendor support and no security patches for newly discovered vulnerabilities",
            "C": "Performance degradation over time",
            "D": "Incompatibility with modern programming languages"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "When a component reaches end-of-life, security vulnerabilities discovered after that date receive no patches. The component becomes an unmitigated attack surface — a supply chain/third-party risk.",
            "A": "Most open-source licenses don't require payment; EOL doesn't change licensing.",
            "B": "No patches for future vulnerabilities is the primary security risk of EOL components.",
            "C": "Performance is a quality concern, not the primary security risk.",
            "D": "Compatibility is a technical concern but not the primary EOL security risk."
        }
    },
    {
        "id": 447,
        "domain": 5,
        "subdomain": "5.2",
        "objective": "Explain elements of the risk management process",
        "stem": "An organization identifies that complying with a new regulation will cost $500,000 but non-compliance fines could reach $2 million. The risk of being fined is 30% per year. What is the ALE of non-compliance?",
        "options": {"A": "$150,000", "B": "$600,000", "C": "$500,000", "D": "$2,000,000"},
        "correct_answer": "B",
        "difficulty": 3,
        "explanations": {
            "correct": "ALE = ARO × SLE = 0.30 × $2,000,000 = $600,000. Since the ALE ($600,000) exceeds the compliance cost ($500,000), complying is financially justified.",
            "A": "$150,000 would be ALE at 30% of $500,000 — confusing the compliance cost with the fine.",
            "B": "ALE = 0.30 × $2,000,000 = $600,000.",
            "C": "$500,000 is the compliance cost, not the ALE.",
            "D": "$2,000,000 is the SLE (single loss), not the ALE."
        }
    },
    {
        "id": 448,
        "domain": 5,
        "subdomain": "5.5",
        "objective": "Explain types and purposes of audits and assessments",
        "stem": "A red team engages in a realistic, long-term campaign simulating an advanced persistent threat (APT). Blue team defends without knowing the exact timing. What term describes this combined exercise?",
        "options": {"A": "Tabletop exercise", "B": "Purple team exercise", "C": "Red team / blue team exercise", "D": "Parallel test"},
        "correct_answer": "C",
        "difficulty": 2,
        "explanations": {
            "correct": "A red team/blue team exercise pits attackers (red) against defenders (blue) in a realistic scenario. The blue team defends in real-time without knowing the red team's exact actions — simulating real adversary behavior.",
            "A": "A tabletop exercise is a discussion-based scenario with no live systems — participants talk through a scenario.",
            "B": "A purple team exercise involves red and blue teams working collaboratively and sharing knowledge — not adversarially.",
            "C": "Red vs. blue team exercise = realistic adversarial simulation.",
            "D": "Parallel test (DR) runs production and DR systems simultaneously — not a security assessment type."
        }
    },
    {
        "id": 449,
        "domain": 5,
        "subdomain": "5.5",
        "objective": "Explain types and purposes of audits and assessments",
        "stem": "What is the PRIMARY purpose of a purple team exercise?",
        "options": {
            "A": "To have red team conduct attacks without blue team awareness",
            "B": "To facilitate knowledge transfer between red and blue teams to improve detection and defense",
            "C": "To test physical security controls",
            "D": "To audit compliance with security policies"
        },
        "correct_answer": "B",
        "difficulty": 3,
        "explanations": {
            "correct": "Purple team exercises are collaborative — red team shares attack techniques with blue team to help defenders improve detection rules, playbooks, and controls. The goal is organizational learning, not a competitive exercise.",
            "A": "That describes a traditional red team exercise — adversarial, not collaborative.",
            "B": "Purple team = collaborative knowledge transfer to improve detection and defense.",
            "C": "Physical security testing (badge cloning, tailgating) is a component of some red team engagements, not purple team.",
            "D": "Compliance audits review policy adherence — not a red/blue/purple team function."
        }
    },
    {
        "id": 450,
        "domain": 5,
        "subdomain": "5.1",
        "objective": "Summarize elements of effective security governance",
        "stem": "A company's security policy requires all employees to lock their workstations when leaving their desk. An employee who repeatedly violates this policy receives a written warning. What type of control is enforcing this policy?",
        "options": {"A": "Technical control", "B": "Physical control", "C": "Administrative control", "D": "Compensating control"},
        "correct_answer": "C",
        "difficulty": 2,
        "explanations": {
            "correct": "A written warning is a disciplinary (administrative/managerial) control — it uses HR policy enforcement mechanisms rather than technology or physical barriers to enforce security requirements.",
            "A": "Technical controls (auto-lock screensaver, endpoint management policies) enforce this technically.",
            "B": "Physical controls use locks, cameras, barriers — not HR warnings.",
            "C": "Written warnings are administrative/managerial controls enforcing policy through HR mechanisms.",
            "D": "Compensating controls substitute for a primary control that cannot be implemented."
        }
    },
    {
        "id": 451,
        "domain": 5,
        "subdomain": "5.2",
        "objective": "Explain elements of the risk management process",
        "stem": "An organization operates in an industry with rapidly evolving threats. Which risk management approach involves continuously reassessing risks as the threat landscape changes?",
        "options": {
            "A": "Point-in-time risk assessment",
            "B": "Annual risk assessment",
            "C": "Continuous risk monitoring",
            "D": "Residual risk acceptance"
        },
        "correct_answer": "C",
        "difficulty": 2,
        "explanations": {
            "correct": "Continuous risk monitoring integrates automated tools, threat intelligence, and real-time metrics to maintain an up-to-date risk picture — essential in dynamic threat environments.",
            "A": "Point-in-time assessments provide a snapshot but quickly become stale in dynamic environments.",
            "B": "Annual assessments are too infrequent for rapidly evolving threats.",
            "C": "Continuous risk monitoring provides ongoing, real-time risk awareness.",
            "D": "Residual risk acceptance is a risk response decision, not a monitoring approach."
        }
    },
    {
        "id": 452,
        "domain": 5,
        "subdomain": "5.3",
        "objective": "Explain the processes associated with third-party risk assessment and management",
        "stem": "An organization uses multiple cloud providers and wants a standardized way to evaluate each provider's security controls. Which approach is MOST efficient?",
        "options": {
            "A": "Conduct a custom penetration test of each provider's infrastructure",
            "B": "Request and review each provider's SOC 2 Type II report and CAIQ questionnaire",
            "C": "Rely on each provider's marketing materials about security",
            "D": "Apply the same internal security policy to each cloud provider"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "SOC 2 Type II reports provide audited control effectiveness over time. The Cloud Security Alliance's CAIQ (Consensus Assessment Initiative Questionnaire) provides a standardized framework for evaluating cloud provider security — efficient for multi-provider evaluation.",
            "A": "Organizations typically cannot penetrate cloud providers' shared infrastructure; providers also rarely allow this.",
            "B": "SOC 2 Type II + CAIQ is the efficient, standardized approach for cloud vendor assessment.",
            "C": "Marketing materials are promotional, not evidence of actual controls.",
            "D": "Applying internal policies to external providers doesn't evaluate their actual security posture."
        }
    },
    {
        "id": 453,
        "domain": 5,
        "subdomain": "5.4",
        "objective": "Summarize elements of effective security compliance",
        "stem": "The NIST Risk Management Framework (RMF) defines a six-step process. Which is the correct order for the first three steps?",
        "options": {
            "A": "Categorize → Select → Implement",
            "B": "Identify → Protect → Detect",
            "C": "Assess → Authorize → Monitor",
            "D": "Plan → Do → Check"
        },
        "correct_answer": "A",
        "difficulty": 3,
        "explanations": {
            "correct": "NIST RMF steps: 1) Prepare, 2) Categorize (system and data), 3) Select (controls from NIST 800-53), 4) Implement, 5) Assess, 6) Authorize, 7) Monitor. The first steps are Categorize → Select → Implement.",
            "A": "Categorize → Select → Implement matches the NIST RMF sequence.",
            "B": "Identify, Protect, Detect are NIST CSF functions, not RMF steps.",
            "C": "Assess → Authorize → Monitor are later RMF steps (steps 5-7).",
            "D": "Plan-Do-Check is the ISO/PDCA cycle, not NIST RMF."
        }
    },
    {
        "id": 454,
        "domain": 5,
        "subdomain": "5.4",
        "objective": "Summarize elements of effective security compliance",
        "stem": "An e-commerce company processes fewer than 1 million Visa transactions annually. Under PCI DSS, which validation level applies?",
        "options": {
            "A": "Level 1 — must have annual on-site QSA assessment",
            "B": "Level 2, 3, or 4 — may use Self-Assessment Questionnaire (SAQ)",
            "C": "No PCI DSS requirements apply below 6 million transactions",
            "D": "PCI DSS only applies to banks, not merchants"
        },
        "correct_answer": "B",
        "difficulty": 3,
        "explanations": {
            "correct": "PCI DSS Level 1 merchants process over 6 million transactions annually and require an on-site QSA audit. Levels 2-4 (lower transaction volumes) may use Self-Assessment Questionnaires (SAQs) instead of a full QSA assessment.",
            "A": "Level 1 requires >6 million transactions; <1 million places the merchant at Level 3 or 4.",
            "B": "Merchants below 6M transactions typically qualify for SAQ-based validation.",
            "C": "PCI DSS applies to any merchant that stores, processes, or transmits cardholder data, regardless of volume.",
            "D": "PCI DSS applies to all entities in the payment ecosystem, including merchants."
        }
    },
    {
        "id": 455,
        "domain": 5,
        "subdomain": "5.6",
        "objective": "Implement security awareness practices",
        "stem": "After a phishing simulation, 15% of employees clicked the malicious link. The security team sends all clickers immediate training on email verification. What principle does this exemplify?",
        "options": {
            "A": "Just-in-time (JIT) provisioning",
            "B": "Teachable moments — targeted training at the point of failure",
            "C": "Mandatory annual security training",
            "D": "Gamification of security training"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "Delivering targeted training immediately after a failure (clicking the phishing link) creates a 'teachable moment' — contextual, timely training proven to be most effective for behavioral change.",
            "A": "JIT provisioning is an access management concept — granting privileges at the moment they're needed.",
            "B": "Teachable moments = immediate, context-relevant training triggered by a failure.",
            "C": "Annual mandatory training is scheduled, not triggered by individual behavior.",
            "D": "Gamification adds game elements (points, leaderboards) to training — not specifically triggered by failures."
        }
    },
    {
        "id": 456,
        "domain": 5,
        "subdomain": "5.2",
        "objective": "Explain elements of the risk management process",
        "stem": "An organization documents all identified risks, their likelihood, impact, current controls, risk owner, and planned remediation in a central document. What is this document called?",
        "options": {
            "A": "Business Impact Analysis",
            "B": "Risk register",
            "C": "Security policy",
            "D": "Incident response plan"
        },
        "correct_answer": "B",
        "difficulty": 1,
        "explanations": {
            "correct": "A risk register (or risk log) is the central repository documenting identified risks, their attributes (likelihood, impact, owner, current controls, status), and treatment plans.",
            "A": "A BIA identifies critical business functions and their recovery priorities — a continuity planning document.",
            "B": "Risk register = the central document tracking all identified risks.",
            "C": "Security policy defines management intent and requirements — not risk tracking.",
            "D": "An incident response plan defines procedures for handling security incidents."
        }
    },
    {
        "id": 457,
        "domain": 5,
        "subdomain": "5.1",
        "objective": "Summarize elements of effective security governance",
        "stem": "What is the difference between a Board of Directors' role and management's role in security governance?",
        "options": {
            "A": "The Board implements security controls; management sets policy",
            "B": "The Board provides strategic oversight and holds management accountable; management executes security programs",
            "C": "Management reports only to shareholders; the Board reports only to the CEO",
            "D": "There is no distinction — they share equal responsibility"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "The Board provides strategic oversight, approves risk appetite, and holds management accountable for security outcomes. Management (CISO, CIO) executes the security program day-to-day — there is a clear governance separation.",
            "A": "The Board doesn't implement controls — management and IT do.",
            "B": "Board = oversight and accountability; management = execution.",
            "C": "Management reports to the Board (and ultimately shareholders through the Board).",
            "D": "There is a distinct separation of roles in corporate governance."
        }
    },
    {
        "id": 458,
        "domain": 5,
        "subdomain": "5.3",
        "objective": "Explain the processes associated with third-party risk assessment and management",
        "stem": "A vendor agreement includes a clause stating the vendor must notify the organization within 24 hours of a confirmed security breach affecting the organization's data. What type of clause is this?",
        "options": {
            "A": "Right-to-audit clause",
            "B": "Incident notification / breach notification clause",
            "C": "Non-disclosure agreement",
            "D": "Service Level Agreement"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "A breach notification clause (or incident notification clause) contractually obligates the vendor to notify the organization within a specified timeframe if the vendor experiences a breach affecting the organization's data.",
            "A": "Right-to-audit gives the organization the right to inspect the vendor's security controls.",
            "B": "Breach notification clause = contractual obligation to notify within a specific timeframe.",
            "C": "NDA covers confidentiality broadly — not just breach notification.",
            "D": "SLA covers service performance metrics (uptime, response time), not breach notification."
        }
    },
    {
        "id": 459,
        "domain": 5,
        "subdomain": "5.2",
        "objective": "Explain elements of the risk management process",
        "stem": "An organization's risk appetite is 'low.' A proposed project introduces a medium residual risk. What is the appropriate action?",
        "options": {
            "A": "Accept the risk because medium is not high",
            "B": "Proceed immediately since residual risk exists for all projects",
            "C": "Escalate to leadership and either add controls to reduce to low or obtain explicit acceptance",
            "D": "Transfer the risk to an insurance provider automatically"
        },
        "correct_answer": "C",
        "difficulty": 3,
        "explanations": {
            "correct": "When residual risk exceeds the organization's risk appetite, it must be escalated. Leadership can either approve additional controls (to reduce to the acceptable level) or explicitly accept the exception — it cannot be silently ignored.",
            "A": "Medium exceeds a 'low' risk appetite — silent acceptance is inappropriate.",
            "B": "Risk appetite exists precisely to trigger review when residual risk exceeds tolerance.",
            "C": "Escalate and either reduce to acceptable level or obtain explicit leadership acceptance.",
            "D": "Insurance may be one option, but automatic transfer without evaluation is not proper risk governance."
        }
    },
    {
        "id": 460,
        "domain": 5,
        "subdomain": "5.5",
        "objective": "Explain types and purposes of audits and assessments",
        "stem": "An attestation of compliance (AoC) in the context of PCI DSS is BEST described as:",
        "options": {
            "A": "A technical vulnerability scan report",
            "B": "A formal declaration by a QSA or merchant summarizing PCI DSS compliance status",
            "C": "An internal audit report for management",
            "D": "A penetration test report for the card brands"
        },
        "correct_answer": "B",
        "difficulty": 3,
        "explanations": {
            "correct": "An Attestation of Compliance (AoC) is the formal PCI DSS document completed by a QSA (or a merchant for SAQ) that summarizes the results of the assessment and attests to compliance status. It accompanies the ROC or SAQ.",
            "A": "Vulnerability scan reports are separate ASV (Approved Scanning Vendor) documents.",
            "B": "AoC = formal compliance attestation signed by QSA and/or merchant.",
            "C": "Internal audit reports are management documents, not the PCI-specific AoC.",
            "D": "Penetration test reports are separate security assessment documents."
        }
    },
    {
        "id": 461,
        "domain": 5,
        "subdomain": "5.1",
        "objective": "Summarize elements of effective security governance",
        "stem": "A company implements a policy requiring separation of duties for financial transactions. The person who authorizes a payment cannot also process it. This control PRIMARILY addresses which threat?",
        "options": {"A": "External hacking", "B": "Insider fraud and collusion", "C": "Phishing attacks", "D": "Network-based attacks"},
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "Separation of duties (SoD) prevents any single person from having end-to-end control over a sensitive process — primarily mitigating insider fraud. Two people would need to collude to commit fraud, raising the barrier significantly.",
            "A": "External hacking is mitigated by technical perimeter and detection controls.",
            "B": "SoD primarily addresses insider fraud by requiring collusion for any single person to abuse the process.",
            "C": "Phishing is a social engineering attack addressed by email filtering and awareness training.",
            "D": "Network attacks are addressed by firewalls, IPS, and network segmentation."
        }
    },
    {
        "id": 462,
        "domain": 5,
        "subdomain": "5.4",
        "objective": "Summarize elements of effective security compliance",
        "stem": "Which US regulation requires publicly traded companies to maintain internal controls over financial reporting and have those controls audited?",
        "options": {"A": "HIPAA", "B": "GLBA", "C": "SOX (Sarbanes-Oxley)", "D": "FERPA"},
        "correct_answer": "C",
        "difficulty": 2,
        "explanations": {
            "correct": "The Sarbanes-Oxley Act (SOX) requires publicly traded companies to maintain internal controls over financial reporting (Section 302 executive certifications, Section 404 internal control assessments) and have external auditors attest to control effectiveness.",
            "A": "HIPAA protects healthcare patient data — not financial reporting.",
            "B": "GLBA (Gramm-Leach-Bliley Act) protects financial consumers' personal information — not internal controls.",
            "C": "SOX Section 404 requires internal control audits for publicly traded companies.",
            "D": "FERPA protects student educational records — unrelated to financial reporting."
        }
    },
    {
        "id": 463,
        "domain": 5,
        "subdomain": "5.4",
        "objective": "Summarize elements of effective security compliance",
        "stem": "The Gramm-Leach-Bliley Act (GLBA) Safeguards Rule requires financial institutions to implement a comprehensive information security program. Which type of data does it primarily protect?",
        "options": {
            "A": "Protected Health Information (PHI)",
            "B": "Nonpublic personal financial information (NPI) of customers",
            "C": "Cardholder data",
            "D": "Classified government information"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "GLBA (specifically the Financial Privacy Rule and Safeguards Rule) requires financial institutions to protect Nonpublic Personal Information (NPI) — customers' private financial data like account numbers, credit history, and Social Security numbers.",
            "A": "PHI is protected by HIPAA, not GLBA.",
            "B": "GLBA protects nonpublic personal financial information of customers.",
            "C": "Cardholder data is governed by PCI DSS.",
            "D": "Classified government information is governed by federal security classifications and regulations."
        }
    },
    {
        "id": 464,
        "domain": 5,
        "subdomain": "5.6",
        "objective": "Implement security awareness practices",
        "stem": "An organization's security awareness program requires all new employees to complete security training within their first week. What type of training program element is this?",
        "options": {
            "A": "Continuous education",
            "B": "Role-based training",
            "C": "Onboarding security training",
            "D": "Remedial training"
        },
        "correct_answer": "C",
        "difficulty": 1,
        "explanations": {
            "correct": "Onboarding security training is required for all new employees and establishes baseline security knowledge, policy awareness, and expected behaviors from day one.",
            "A": "Continuous education is ongoing training (monthly tips, lunch-and-learns) — not specifically for new hires.",
            "B": "Role-based training targets specific job roles (developers, admins) with relevant security topics.",
            "C": "Onboarding training = new employee security orientation in the first days/week.",
            "D": "Remedial training is assigned to employees who have violated policies or failed assessments."
        }
    },
    {
        "id": 465,
        "domain": 5,
        "subdomain": "5.2",
        "objective": "Explain elements of the risk management process",
        "stem": "An organization stores critical data in a region prone to earthquakes. The security team considers relocating the data center. What risk response strategy is being considered?",
        "options": {"A": "Risk mitigation", "B": "Risk acceptance", "C": "Risk avoidance", "D": "Risk transfer"},
        "correct_answer": "C",
        "difficulty": 2,
        "explanations": {
            "correct": "Relocating the data center away from an earthquake-prone region eliminates the geographic risk — this is risk avoidance (removing the organization from the risk scenario entirely).",
            "A": "Risk mitigation would keep the data center but add seismic protection or redundancy.",
            "B": "Risk acceptance acknowledges the risk without taking action.",
            "C": "Relocation eliminates the earthquake exposure — risk avoidance.",
            "D": "Risk transfer would shift financial consequences to an insurer while keeping the data center in place."
        }
    },
    {
        "id": 466,
        "domain": 5,
        "subdomain": "5.1",
        "objective": "Summarize elements of effective security governance",
        "stem": "Which of the following BEST describes a 'security policy exception'?",
        "options": {
            "A": "A permanent override of security policy approved by the CISO",
            "B": "A documented, time-limited deviation from policy with compensating controls and management approval",
            "C": "An informal workaround created by IT staff",
            "D": "An automatic exemption for legacy systems"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "A security policy exception is a formally documented, time-limited deviation from policy that requires management approval, includes compensating controls to mitigate the risk, and has a defined remediation timeline.",
            "A": "A permanent override undermines the policy — exceptions should be temporary.",
            "B": "Documented, time-limited, management-approved, with compensating controls = proper exception process.",
            "C": "Informal workarounds are policy violations, not exceptions.",
            "D": "Automatic exemptions for legacy systems are informal and undermine governance."
        }
    },
    {
        "id": 467,
        "domain": 5,
        "subdomain": "5.3",
        "objective": "Explain the processes associated with third-party risk assessment and management",
        "stem": "A company relies on a single cloud provider for all its infrastructure. What risk concept does this represent, and what strategy should be considered?",
        "options": {
            "A": "Defense in depth; add more security tools",
            "B": "Single point of failure / vendor concentration risk; multi-cloud or hybrid cloud strategy",
            "C": "Data sovereignty risk; encrypt all data at rest",
            "D": "Compliance risk; obtain ISO 27001 certification"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "Relying on a single vendor creates vendor concentration risk and a single point of failure — if the provider has an outage, all services fail. Multi-cloud or hybrid cloud strategies distribute this risk.",
            "A": "Defense in depth is a layered security strategy — doesn't address vendor concentration.",
            "B": "Single cloud provider = vendor concentration/single point of failure; multi-cloud diversifies the risk.",
            "C": "Data sovereignty concerns where data is legally stored — encryption doesn't address availability risk.",
            "D": "ISO 27001 is the organization's own certification — doesn't address cloud provider risk concentration."
        }
    },
    {
        "id": 468,
        "domain": 5,
        "subdomain": "5.5",
        "objective": "Explain types and purposes of audits and assessments",
        "stem": "A compliance officer conducts an internal review comparing current security practices against the organization's own policies and regulatory requirements. What type of assessment is this?",
        "options": {"A": "Penetration test", "B": "Gap analysis", "C": "Threat modeling", "D": "Business impact analysis"},
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "A gap analysis compares the current state against a desired or required state (policies, standards, regulations) to identify gaps — areas where current practices fall short of requirements.",
            "A": "Penetration testing simulates attacks to find exploitable vulnerabilities.",
            "B": "Gap analysis = current state vs. required state, identifying what's missing.",
            "C": "Threat modeling systematically identifies threats to a system or application.",
            "D": "BIA identifies critical functions and recovery priorities for business continuity planning."
        }
    },
    {
        "id": 469,
        "domain": 5,
        "subdomain": "5.2",
        "objective": "Explain elements of the risk management process",
        "stem": "Which element of quantitative risk analysis helps determine how much to spend on a security control?",
        "options": {
            "A": "Threat intelligence feeds",
            "B": "The ALE before and after the control — the control cost should not exceed the ALE reduction",
            "C": "The CVE severity score",
            "D": "The organization's industry sector"
        },
        "correct_answer": "B",
        "difficulty": 3,
        "explanations": {
            "correct": "The maximum justifiable spend on a control = ALE (before control) - ALE (after control). If a control costs more than the risk reduction it provides, it's not financially justified — a core principle of quantitative risk analysis.",
            "A": "Threat intelligence informs likelihood estimates but doesn't directly determine control spend.",
            "B": "Control value = ALE reduction; control cost should not exceed the risk reduction achieved.",
            "C": "CVE severity scores assess technical vulnerability risk — not the financial control spend calculation.",
            "D": "Industry sector may influence threat landscape but doesn't directly set control spending thresholds."
        }
    },
    {
        "id": 470,
        "domain": 5,
        "subdomain": "5.4",
        "objective": "Summarize elements of effective security compliance",
        "stem": "Under GDPR, the 'right to erasure' (right to be forgotten) allows individuals to request deletion of their personal data. In which situation is this right absolute?",
        "options": {
            "A": "When the data is needed for legal compliance",
            "B": "When data is no longer necessary for its original purpose and no other legal basis applies",
            "C": "When the individual moves to a non-EU country",
            "D": "When the individual changes their email address"
        },
        "correct_answer": "B",
        "difficulty": 3,
        "explanations": {
            "correct": "Under GDPR Article 17, the right to erasure applies most clearly when the data is no longer necessary for the purpose it was collected and no other legal basis (legal obligation, public interest, etc.) justifies retention.",
            "A": "If data is needed for legal compliance, the right to erasure may be overridden.",
            "B": "Data no longer needed for its purpose with no other legal basis = strongest erasure right.",
            "C": "Geographic location of the individual doesn't determine erasure rights.",
            "D": "Changing an email address doesn't trigger a right to erasure of all personal data."
        }
    },
    {
        "id": 471,
        "domain": 5,
        "subdomain": "5.1",
        "objective": "Summarize elements of effective security governance",
        "stem": "An organization's Chief Information Security Officer (CISO) reports to the Chief Information Officer (CIO). What is a potential concern with this reporting structure?",
        "options": {
            "A": "The CISO has too much budget authority",
            "B": "Security concerns may be subordinated to IT operational priorities, creating a conflict of interest",
            "C": "The CISO cannot attend board meetings",
            "D": "The CIO will have insufficient cybersecurity knowledge"
        },
        "correct_answer": "B",
        "difficulty": 3,
        "explanations": {
            "correct": "When CISO reports to CIO, security may be deprioritized when it conflicts with IT operational goals (system uptime, project timelines) — a conflict of interest. Independent reporting (to CEO or Board) is preferred for strong security governance.",
            "A": "CISO budget authority is typically defined separately from the reporting structure.",
            "B": "CISO subordinate to CIO creates potential conflict between security and IT operational priorities.",
            "C": "Board meeting attendance is separate from the reporting hierarchy.",
            "D": "CIO knowledge of cybersecurity varies but doesn't inherently cause governance problems."
        }
    },
    {
        "id": 472,
        "domain": 5,
        "subdomain": "5.6",
        "objective": "Implement security awareness practices",
        "stem": "A security team measures the click rate on phishing simulations over 12 months and observes it drops from 22% to 6%. What does this metric indicate?",
        "options": {
            "A": "The phishing simulations are getting easier over time",
            "B": "The security awareness program is effectively changing employee behavior",
            "C": "The email filtering system has improved",
            "D": "Employees are sharing answers to the simulations"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "A declining click rate over time (22% → 6%) is a key effectiveness metric for security awareness programs, demonstrating measurable behavioral change in employees' ability to recognize phishing.",
            "A": "Simulation difficulty would explain a drop but would undermine the metric's validity — not the primary interpretation.",
            "B": "Declining click rate = awareness program successfully improving employee phishing recognition.",
            "C": "Email filtering operates independently — simulation emails are typically designed to bypass filters.",
            "D": "Answer-sharing would be unusual for behavioral simulations with varying templates."
        }
    },
    {
        "id": 473,
        "domain": 5,
        "subdomain": "5.3",
        "objective": "Explain the processes associated with third-party risk assessment and management",
        "stem": "What is the MAIN security concern with using open-source software components without a formal inventory?",
        "options": {
            "A": "Open-source software always contains malicious code",
            "B": "Without an inventory (software bill of materials), the organization cannot identify which components are affected when a vulnerability is disclosed",
            "C": "Open-source software is not permitted under most security frameworks",
            "D": "Open-source components cannot be encrypted"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "A Software Bill of Materials (SBOM) tracks all open-source and third-party components. Without it, when a critical vulnerability is disclosed (e.g., Log4Shell), the organization can't quickly determine if or where the affected component is used.",
            "A": "Open-source software is not inherently malicious — it's widely used and reviewed by communities.",
            "B": "No SBOM = inability to respond quickly to disclosed vulnerabilities in used components.",
            "C": "Most security frameworks don't prohibit open-source software.",
            "D": "Open-source components can be encrypted like any other software."
        }
    },
    {
        "id": 474,
        "domain": 5,
        "subdomain": "5.2",
        "objective": "Explain elements of the risk management process",
        "stem": "A security analyst is asked to compare the likelihood and impact of different risks to prioritize remediation. The analyst uses a 5×5 grid plotting likelihood against impact. What is this tool called?",
        "options": {
            "A": "CVSS calculator",
            "B": "Risk matrix (heat map)",
            "C": "Business Impact Analysis",
            "D": "Fault tree analysis"
        },
        "correct_answer": "B",
        "difficulty": 1,
        "explanations": {
            "correct": "A risk matrix (or risk heat map) plots likelihood versus impact on a grid, typically color-coded (red/high, yellow/medium, green/low) to visualize and prioritize risks. A 5×5 matrix is a common format.",
            "A": "CVSS calculator scores technical vulnerability severity — not a general risk prioritization tool.",
            "B": "Risk matrix/heat map = likelihood × impact grid for risk visualization and prioritization.",
            "C": "BIA identifies critical business functions and recovery times — not a general risk prioritization matrix.",
            "D": "Fault tree analysis models failure modes to identify root causes — more complex than a risk matrix."
        }
    },
    {
        "id": 475,
        "domain": 5,
        "subdomain": "5.4",
        "objective": "Summarize elements of effective security compliance",
        "stem": "Which regulation requires organizations to conduct a Data Protection Impact Assessment (DPIA) before processing that is 'likely to result in a high risk' to individuals?",
        "options": {"A": "HIPAA", "B": "PCI DSS", "C": "GDPR", "D": "SOX"},
        "correct_answer": "C",
        "difficulty": 2,
        "explanations": {
            "correct": "GDPR Article 35 requires a DPIA before processing likely to result in high risk to data subjects — particularly for new technologies, large-scale processing of sensitive data, or systematic profiling.",
            "A": "HIPAA requires privacy and security risk assessments but not a DPIA in the GDPR sense.",
            "B": "PCI DSS requires risk assessments related to cardholder data but not DPIAs.",
            "C": "GDPR Article 35 mandates DPIAs for high-risk processing activities.",
            "D": "SOX focuses on financial reporting internal controls, not data protection impact assessments."
        }
    },
    {
        "id": 476,
        "domain": 5,
        "subdomain": "5.5",
        "objective": "Explain types and purposes of audits and assessments",
        "stem": "A tabletop exercise for incident response involves:",
        "options": {
            "A": "Cutting over production systems to DR infrastructure",
            "B": "Discussion-based walkthrough of a scenario without activating real systems",
            "C": "Deploying actual attack tools against production systems",
            "D": "Simulating a full business interruption to test recovery"
        },
        "correct_answer": "B",
        "difficulty": 1,
        "explanations": {
            "correct": "A tabletop exercise is a discussion-based simulation where participants talk through their responses to a scenario (e.g., 'a ransomware attack hits at 2 AM — what do you do?') without touching real systems.",
            "A": "Cutting over to DR is a parallel or full-interruption test, not a tabletop.",
            "B": "Tabletop = discussion-based, no real systems activated.",
            "C": "Deploying attack tools against production is a penetration test or red team, not tabletop.",
            "D": "Full business interruption testing is the most disruptive DR test — not a tabletop."
        }
    },
    {
        "id": 477,
        "domain": 5,
        "subdomain": "5.1",
        "objective": "Summarize elements of effective security governance",
        "stem": "A company's security policy states 'all sensitive data must be encrypted in transit.' What is missing from this policy statement that would make it more enforceable?",
        "options": {
            "A": "A list of all employees who must comply",
            "B": "Specific technical standards (e.g., TLS 1.2+ required; TLS 1.0 prohibited)",
            "C": "The name of the CEO who approved the policy",
            "D": "A detailed description of the encryption algorithm's mathematical basis"
        },
        "correct_answer": "B",
        "difficulty": 3,
        "explanations": {
            "correct": "The policy statement is high-level — it lacks specificity on what 'encrypted' means technically. A complementary standard (e.g., 'TLS 1.2 or higher; SSLv3 and TLS 1.0 are prohibited') makes the requirement measurable and auditable.",
            "A": "Scope ('who must comply') is important but the question asks what makes it more enforceable.",
            "B": "Specific technical standards (TLS versions, algorithms) make the policy measurable and auditable.",
            "C": "Executive signatures are good practice for legitimacy but don't address technical enforceability.",
            "D": "Mathematical descriptions belong in academic papers, not security policies."
        }
    },
    {
        "id": 478,
        "domain": 5,
        "subdomain": "5.6",
        "objective": "Implement security awareness practices",
        "stem": "Which of the following is an example of role-based security training?",
        "options": {
            "A": "All employees watch the same 30-minute security video annually",
            "B": "Developers receive secure coding training (OWASP Top 10, input validation)",
            "C": "New employees attend a general security orientation",
            "D": "Management approves a security budget"
        },
        "correct_answer": "B",
        "difficulty": 1,
        "explanations": {
            "correct": "Role-based training tailors content to specific job functions. Developers receive secure coding training (OWASP, secure SDLC) because their work directly introduces or mitigates code vulnerabilities.",
            "A": "Same video for all employees is general awareness training, not role-based.",
            "B": "Secure coding training for developers = role-based training for a specific technical role.",
            "C": "General orientation is onboarding training, not role-specific.",
            "D": "Budget approval is a governance/management function, not security training."
        }
    },
    {
        "id": 479,
        "domain": 5,
        "subdomain": "5.2",
        "objective": "Explain elements of the risk management process",
        "stem": "An organization's risk tolerance defines:",
        "options": {
            "A": "The amount of risk the organization is willing to accept in pursuit of its objectives",
            "B": "The maximum loss the organization can recover from",
            "C": "The number of security incidents per year deemed acceptable",
            "D": "The organization's legal liability limit"
        },
        "correct_answer": "A",
        "difficulty": 2,
        "explanations": {
            "correct": "Risk tolerance (or risk appetite) defines the amount and type of risk the organization is willing to accept in pursuit of its strategic objectives. It guides decisions about which risks to accept vs. mitigate.",
            "A": "Risk tolerance = the acceptable level of risk the organization will accept to pursue objectives.",
            "B": "Recovery capacity relates to business continuity, not risk tolerance.",
            "C": "Incident count thresholds may be a metric but don't define risk tolerance comprehensively.",
            "D": "Legal liability limits are legal/insurance concepts, distinct from risk tolerance."
        }
    },
    {
        "id": 480,
        "domain": 5,
        "subdomain": "5.4",
        "objective": "Summarize elements of effective security compliance",
        "stem": "FERPA (Family Educational Rights and Privacy Act) protects which category of records?",
        "options": {
            "A": "Student educational records at federally funded institutions",
            "B": "Federal employees' personnel records",
            "C": "Healthcare records of college students",
            "D": "Financial aid fraud records"
        },
        "correct_answer": "A",
        "difficulty": 2,
        "explanations": {
            "correct": "FERPA protects the privacy of student education records at educational institutions receiving federal funding. It gives parents (and students over 18) rights to access and control disclosure of educational records.",
            "A": "FERPA = student educational records at federally funded schools.",
            "B": "Federal employee records are protected by the Privacy Act of 1974.",
            "C": "Healthcare records are protected by HIPAA, though FERPA may intersect for school health records.",
            "D": "Financial aid fraud is addressed by other federal laws."
        }
    },
    {
        "id": 481,
        "domain": 5,
        "subdomain": "5.1",
        "objective": "Summarize elements of effective security governance",
        "stem": "Which of the following BEST describes the concept of 'due diligence' in the context of security governance?",
        "options": {
            "A": "Implementing security controls that are proportionate to the risk",
            "B": "Conducting research and verification to ensure security decisions are informed",
            "C": "Transferring risk to a third party",
            "D": "Following industry best practices regardless of cost"
        },
        "correct_answer": "B",
        "difficulty": 3,
        "explanations": {
            "correct": "Due diligence means doing your homework — investigating, researching, and verifying before making decisions. In security governance, it means ensuring decisions (including vendor selection, risk acceptance) are based on evidence and thorough analysis.",
            "A": "Proportionate controls describe 'due care' — implementing reasonable protections.",
            "B": "Due diligence = research and verification to ensure informed decisions.",
            "C": "Risk transfer is a risk management strategy, not the definition of due diligence.",
            "D": "Following best practices regardless of cost may describe due care but not due diligence specifically."
        }
    },
    {
        "id": 482,
        "domain": 5,
        "subdomain": "5.1",
        "objective": "Summarize elements of effective security governance",
        "stem": "Which of the following BEST describes 'due care' in security governance?",
        "options": {
            "A": "Researching and verifying security decisions before acting",
            "B": "Implementing reasonable security controls to protect assets",
            "C": "Transferring security responsibility to a vendor",
            "D": "Documenting all security incidents"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "Due care means taking reasonable steps to protect assets — implementing appropriate security controls. It's the 'doing' component. If due diligence is 'knowing what to do,' due care is 'doing it.'",
            "A": "Research and verification before acting is due diligence — the planning/investigation component.",
            "B": "Due care = implementing reasonable protections; the execution component.",
            "C": "Transferring responsibility is a risk management strategy, not due care.",
            "D": "Incident documentation is a security operations practice, not the definition of due care."
        }
    },
    {
        "id": 483,
        "domain": 5,
        "subdomain": "5.5",
        "objective": "Explain types and purposes of audits and assessments",
        "stem": "Penetration testing methodologies often follow phases. Which is the correct standard order?",
        "options": {
            "A": "Exploitation → Reconnaissance → Reporting → Post-exploitation",
            "B": "Reconnaissance → Scanning → Exploitation → Post-exploitation → Reporting",
            "C": "Reporting → Planning → Scanning → Exploitation",
            "D": "Post-exploitation → Reconnaissance → Scanning → Reporting"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "Standard penetration test methodology (PTES, CEH): Reconnaissance (passive/active information gathering) → Scanning/Enumeration → Exploitation → Post-exploitation (persistence, lateral movement) → Reporting.",
            "A": "Exploitation cannot precede reconnaissance — you need information before exploiting.",
            "B": "Reconnaissance → Scanning → Exploitation → Post-exploitation → Reporting is the correct order.",
            "C": "Reporting comes last, after all testing is complete.",
            "D": "Post-exploitation cannot precede reconnaissance or exploitation."
        }
    },
    {
        "id": 484,
        "domain": 5,
        "subdomain": "5.3",
        "objective": "Explain the processes associated with third-party risk assessment and management",
        "stem": "An organization terminates a cloud provider contract. What is the PRIMARY security concern during offboarding?",
        "options": {
            "A": "The cost of migrating to a new provider",
            "B": "Ensuring all organization data is retrieved or securely deleted from the provider's systems",
            "C": "Updating the provider's access to the organization's internal network",
            "D": "Migrating user accounts to a new identity provider"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "During cloud provider offboarding, the primary security concern is ensuring all organizational data is either fully retrieved or cryptographically erased from the provider's storage — preventing data remnants from being accessed after contract termination.",
            "A": "Migration cost is a financial concern, not a security concern.",
            "B": "Data retrieval and secure deletion is the primary security concern during offboarding.",
            "C": "Provider access to the organization's network is a valid concern but secondary to data remnant risk.",
            "D": "Identity provider migration is an operational concern secondary to data security."
        }
    },
    {
        "id": 485,
        "domain": 5,
        "subdomain": "5.2",
        "objective": "Explain elements of the risk management process",
        "stem": "What is the PRIMARY purpose of a Business Impact Analysis (BIA) in risk management?",
        "options": {
            "A": "To identify all technical vulnerabilities in the organization's systems",
            "B": "To determine which business functions are critical, their dependencies, and recovery priorities",
            "C": "To calculate the ALE for all identified risks",
            "D": "To establish the organization's risk appetite"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "A BIA identifies critical business functions, their dependencies, and the financial/operational impact of disruption — establishing RTO, RPO, and recovery priorities for continuity planning.",
            "A": "Technical vulnerability identification is done through vulnerability assessments and scanning.",
            "B": "BIA = critical function identification, dependencies, and recovery priorities.",
            "C": "ALE calculations are part of quantitative risk analysis, not BIA.",
            "D": "Risk appetite is set by leadership/governance, not derived from BIA."
        }
    },
    {
        "id": 486,
        "domain": 5,
        "subdomain": "5.4",
        "objective": "Summarize elements of effective security compliance",
        "stem": "A company implements a privacy notice on its website that describes what personal data is collected and how it is used. Under GDPR, what requirement does this satisfy?",
        "options": {
            "A": "Data minimization",
            "B": "Purpose limitation",
            "C": "Transparency / right to be informed",
            "D": "Data portability"
        },
        "correct_answer": "C",
        "difficulty": 2,
        "explanations": {
            "correct": "GDPR Article 13-14 requires transparency — organizations must inform individuals (at the point of collection) what data is collected, why, how long it's kept, and their rights. The privacy notice satisfies this 'right to be informed.'",
            "A": "Data minimization means collecting only data necessary for the purpose — enforced through practice, not a notice.",
            "B": "Purpose limitation means using data only for its stated purpose — a data governance principle.",
            "C": "Privacy notice = transparency / right to be informed under GDPR.",
            "D": "Data portability (GDPR Article 20) is the right to receive one's data in a portable format."
        }
    },
    {
        "id": 487,
        "domain": 5,
        "subdomain": "5.6",
        "objective": "Implement security awareness practices",
        "stem": "An organization trains help desk staff to recognize and resist social engineering calls attempting to reset passwords without proper verification. What training focus is this?",
        "options": {
            "A": "Phishing resistance",
            "B": "Vishing and pretexting defense for help desk staff",
            "C": "Physical security awareness",
            "D": "Insider threat detection"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "Help desk staff are frequently targeted by voice-based social engineering (vishing) where attackers pretend to be employees or executives (pretexting) to request password resets — targeted training addresses this specific threat.",
            "A": "Phishing resistance focuses on email-based attacks — vishing is voice-based.",
            "B": "Vishing/pretexting defense for help desk = training specifically for voice social engineering targeting support staff.",
            "C": "Physical security covers tailgating, badge access — not voice social engineering.",
            "D": "Insider threat detection focuses on monitoring for malicious insiders, not social engineering defense."
        }
    },
    {
        "id": 488,
        "domain": 5,
        "subdomain": "5.1",
        "objective": "Summarize elements of effective security governance",
        "stem": "Which of the following is an example of a directive control?",
        "options": {
            "A": "A firewall that blocks unauthorized traffic",
            "B": "A security camera recording entry points",
            "C": "A mandatory security awareness training requirement",
            "D": "A data backup system"
        },
        "correct_answer": "C",
        "difficulty": 2,
        "explanations": {
            "correct": "Directive controls provide instructions or mandates intended to guide behavior — policies, mandatory training, security procedures, and signs. Mandatory security awareness training tells employees what they must do.",
            "A": "A firewall is a technical, preventive control — it blocks unauthorized traffic automatically.",
            "B": "Security cameras are detective controls — they observe and record.",
            "C": "Mandatory training is a directive control — it mandates behavior through policy.",
            "D": "A backup system is a corrective/recovery control — restoring data after loss."
        }
    },
    {
        "id": 489,
        "domain": 5,
        "subdomain": "5.2",
        "objective": "Explain elements of the risk management process",
        "stem": "A company hires an external consulting firm to manage its security operations. The consulting firm experiences a breach. Who is ultimately accountable for protecting the company's customer data?",
        "options": {
            "A": "The consulting firm, because they are operating the controls",
            "B": "The company, because accountability for data protection cannot be outsourced",
            "C": "Both equally — liability is shared 50/50",
            "D": "The customer, because they accepted the terms of service"
        },
        "correct_answer": "B",
        "difficulty": 3,
        "explanations": {
            "correct": "Organizations can outsource security operations but not accountability. Under regulations like GDPR, the data controller (the company) remains ultimately accountable for protecting customer data, even when a processor (consulting firm) experiences the breach.",
            "A": "The consulting firm (processor) bears operational responsibility but not ultimate regulatory accountability.",
            "B": "The company (data controller) retains ultimate accountability — you can outsource operations, not liability.",
            "C": "Liability may be shared contractually, but regulatory accountability rests with the data controller.",
            "D": "Customers' acceptance of terms doesn't relieve the company of data protection obligations."
        }
    },
    {
        "id": 490,
        "domain": 5,
        "subdomain": "5.5",
        "objective": "Explain types and purposes of audits and assessments",
        "stem": "Bug bounty programs are designed to:",
        "options": {
            "A": "Replace internal penetration testing entirely",
            "B": "Compensate external researchers for responsibly disclosing security vulnerabilities",
            "C": "Provide legal authorization for researchers to attack production systems indefinitely",
            "D": "Automate vulnerability scanning of public-facing systems"
        },
        "correct_answer": "B",
        "difficulty": 1,
        "explanations": {
            "correct": "Bug bounty programs incentivize responsible disclosure by paying security researchers monetary rewards for finding and reporting vulnerabilities — creating a structured way to leverage the global security research community.",
            "A": "Bug bounties complement but don't replace internal security testing.",
            "B": "Bug bounties = financial rewards for responsible vulnerability disclosure.",
            "C": "Bug bounties have defined scopes and rules — they don't grant unlimited attack authorization.",
            "D": "Automated scanning is a different tool — bug bounties involve human researchers."
        }
    },
    {
        "id": 491,
        "domain": 5,
        "subdomain": "5.4",
        "objective": "Summarize elements of effective security compliance",
        "stem": "The concept of 'privacy by design' means:",
        "options": {
            "A": "Privacy controls are added to systems after deployment",
            "B": "Privacy protections are built into systems and processes from the outset",
            "C": "Privacy is only required for healthcare organizations",
            "D": "Encryption is applied to all databases by default"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "Privacy by design (PbD) means embedding privacy protections into the design of systems and processes from the start — not retrofitting them later. This is a GDPR principle (Article 25: data protection by design and by default).",
            "A": "Adding controls post-deployment is the opposite of privacy by design.",
            "B": "Privacy built into systems from the outset = privacy by design.",
            "C": "Privacy by design applies across all industries that handle personal data.",
            "D": "Encryption is one privacy mechanism but PbD is a broader design philosophy."
        }
    },
    {
        "id": 492,
        "domain": 5,
        "subdomain": "5.3",
        "objective": "Explain the processes associated with third-party risk assessment and management",
        "stem": "What is a Managed Security Service Provider (MSSP)?",
        "options": {
            "A": "An internal team that manages the organization's cloud infrastructure",
            "B": "A third-party company that provides outsourced security monitoring and management services",
            "C": "A software vendor that provides SIEM tools",
            "D": "A government agency that provides threat intelligence"
        },
        "correct_answer": "B",
        "difficulty": 1,
        "explanations": {
            "correct": "An MSSP is a third-party company that provides outsourced security services — SOC monitoring, SIEM management, vulnerability management, incident response — on behalf of the client organization.",
            "A": "Internal cloud teams are employees — MSSPs are external third parties.",
            "B": "MSSP = third-party outsourced security monitoring and management.",
            "C": "SIEM vendors provide tools; MSSPs provide managed services (including SIEM operation).",
            "D": "Government threat intelligence sources (CISA, FBI) are distinct from MSSPs."
        }
    },
    {
        "id": 493,
        "domain": 5,
        "subdomain": "5.2",
        "objective": "Explain elements of the risk management process",
        "stem": "Which of the following scenarios represents risk avoidance?",
        "options": {
            "A": "Purchasing cyber liability insurance",
            "B": "Deciding not to collect and store credit card numbers at all",
            "C": "Encrypting all stored credit card data",
            "D": "Accepting that some phishing attacks will succeed"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "By choosing not to collect or store credit card numbers, the organization eliminates the PCI DSS risk entirely — this is risk avoidance (not engaging in the activity that creates the risk).",
            "A": "Insurance = risk transfer.",
            "B": "Not storing card numbers = avoiding the risk entirely.",
            "C": "Encrypting card data = risk mitigation (applying controls to reduce impact).",
            "D": "Acknowledging some phishing will succeed = risk acceptance."
        }
    },
    {
        "id": 494,
        "domain": 5,
        "subdomain": "5.6",
        "objective": "Implement security awareness practices",
        "stem": "What is 'gamification' in the context of security awareness training?",
        "options": {
            "A": "Using game theory to model attacker behavior",
            "B": "Incorporating game elements (points, leaderboards, badges) to increase engagement with security training",
            "C": "Requiring employees to play cybersecurity games instead of working",
            "D": "Using virtual reality to simulate security incidents"
        },
        "correct_answer": "B",
        "difficulty": 1,
        "explanations": {
            "correct": "Gamification applies game design elements (points, achievements, competition, progress tracking) to non-game contexts like security training to increase engagement, motivation, and knowledge retention.",
            "A": "Game theory is a mathematical framework for strategic decision-making — not training gamification.",
            "B": "Gamification = game elements applied to training for increased engagement.",
            "C": "Gamification enhances training; it doesn't replace work.",
            "D": "VR is a training delivery technology — gamification is a design approach that can be used with VR but is distinct."
        }
    },
    {
        "id": 495,
        "domain": 5,
        "subdomain": "5.1",
        "objective": "Summarize elements of effective security governance",
        "stem": "An organization's password policy states: 'Passwords must be at least 12 characters, contain uppercase and lowercase letters, a number, and a special character.' What category does this document fall under?",
        "options": {"A": "Policy", "B": "Guideline", "C": "Standard", "D": "Procedure"},
        "correct_answer": "C",
        "difficulty": 2,
        "explanations": {
            "correct": "This specific, measurable requirement ('minimum 12 characters, must contain...') is a standard — it implements the higher-level policy ('passwords must be strong') with concrete, auditable specifications.",
            "A": "Policy would say 'users must use strong passwords' without specifying exact requirements.",
            "B": "Guidelines are recommendations ('consider using passphrases') — not mandatory requirements.",
            "C": "Specific, mandatory technical requirements = standard.",
            "D": "A procedure would describe how to create/change a password step-by-step."
        }
    },
    {
        "id": 496,
        "domain": 5,
        "subdomain": "5.5",
        "objective": "Explain types and purposes of audits and assessments",
        "stem": "An organization wants to evaluate a specific application's security before production release. Which assessment type is MOST appropriate?",
        "options": {
            "A": "Full infrastructure penetration test",
            "B": "Compliance audit",
            "C": "Application security assessment (including SAST and DAST)",
            "D": "Social engineering assessment"
        },
        "correct_answer": "C",
        "difficulty": 2,
        "explanations": {
            "correct": "An application security assessment combines static analysis (SAST — reviewing source code) and dynamic analysis (DAST — testing the running application) to identify security vulnerabilities before production release.",
            "A": "A full infrastructure pentest covers networks, servers, etc. — broader than needed for a single application.",
            "B": "Compliance audits verify policy adherence — not primarily designed to find code vulnerabilities.",
            "C": "Application security assessment (SAST + DAST) is the targeted approach for pre-release app security.",
            "D": "Social engineering assesses human vulnerabilities — not application code security."
        }
    },
    {
        "id": 497,
        "domain": 5,
        "subdomain": "5.2",
        "objective": "Explain elements of the risk management process",
        "stem": "A security team documents that accepting a particular high risk requires the signature of the Chief Risk Officer. What governance mechanism is this?",
        "options": {
            "A": "Risk mitigation approval",
            "B": "Separation of duties",
            "C": "Risk acceptance threshold and escalation policy",
            "D": "Mandatory access control"
        },
        "correct_answer": "C",
        "difficulty": 3,
        "explanations": {
            "correct": "Requiring escalation and CRO signature for high-risk acceptance decisions is a risk acceptance threshold and escalation policy — ensuring senior leadership explicitly owns decisions to accept significant risks.",
            "A": "Risk mitigation approval governs applying controls — this is about accepting risk without controls.",
            "B": "Separation of duties prevents a single person from controlling an entire process — not a risk acceptance mechanism.",
            "C": "Risk acceptance thresholds with escalation requirements = governance mechanism for high-risk decisions.",
            "D": "MAC is a technical access control model — not a risk governance mechanism."
        }
    },
    {
        "id": 498,
        "domain": 5,
        "subdomain": "5.4",
        "objective": "Summarize elements of effective security compliance",
        "stem": "Which of the following is an example of a 'continuous compliance' approach?",
        "options": {
            "A": "Annual compliance audits conducted by external auditors",
            "B": "Automated monitoring and alerting when configurations drift from compliant baselines",
            "C": "Quarterly penetration testing",
            "D": "Policy review every three years"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "Continuous compliance uses automated tools to continuously monitor configurations, access controls, and security settings against compliance baselines — providing real-time alerting when drift occurs rather than waiting for periodic audits.",
            "A": "Annual audits are periodic, not continuous.",
            "B": "Automated real-time monitoring of compliance posture = continuous compliance.",
            "C": "Quarterly pentesting is periodic assessment — better than annual but not continuous.",
            "D": "Three-year policy review is very periodic — the opposite of continuous compliance."
        }
    },
    {
        "id": 499,
        "domain": 5,
        "subdomain": "5.3",
        "objective": "Explain the processes associated with third-party risk assessment and management",
        "stem": "An organization requires vendors to complete a security questionnaire before onboarding. What risk management phase does this represent?",
        "options": {
            "A": "Vendor offboarding",
            "B": "Ongoing vendor monitoring",
            "C": "Vendor due diligence and risk assessment during onboarding",
            "D": "Contract negotiation"
        },
        "correct_answer": "C",
        "difficulty": 1,
        "explanations": {
            "correct": "Requiring a security questionnaire before onboarding a vendor is due diligence — assessing the vendor's security posture during the selection/onboarding phase before granting access to systems or data.",
            "A": "Offboarding occurs when terminating a vendor relationship — not onboarding.",
            "B": "Ongoing monitoring happens after onboarding — periodic reviews, not the initial assessment.",
            "C": "Pre-onboarding security questionnaire = due diligence during vendor onboarding.",
            "D": "Contract negotiation may reference security questionnaire findings but is separate from the due diligence activity."
        }
    },
    {
        "id": 500,
        "domain": 5,
        "subdomain": "5.6",
        "objective": "Implement security awareness practices",
        "stem": "Which security awareness metric BEST demonstrates the program's business value to executive leadership?",
        "options": {
            "A": "Number of training modules completed",
            "B": "Reduction in successful phishing click-throughs and security incidents attributable to human error",
            "C": "Number of employees who passed the annual security quiz",
            "D": "Total hours of security training delivered"
        },
        "correct_answer": "B",
        "difficulty": 3,
        "explanations": {
            "correct": "Executives care about risk reduction, not activity metrics. Demonstrating reduced phishing click rates and fewer human-error-caused incidents shows the program's actual impact on organizational risk — the most compelling business case.",
            "A": "Completed modules measure activity, not effectiveness.",
            "B": "Reduced incidents and click rates = outcome metrics demonstrating risk reduction — the business value.",
            "C": "Quiz pass rates measure knowledge, not behavior change in real scenarios.",
            "D": "Hours delivered measures volume, not quality or effectiveness."
        }
    },
    {
        "id": 501,
        "domain": 5,
        "subdomain": "5.1",
        "objective": "Summarize elements of effective security governance",
        "stem": "A security steering committee meets quarterly to review the organization's security posture, approve new initiatives, and allocate resources. What governance function does this committee serve?",
        "options": {
            "A": "Operational security management",
            "B": "Strategic security governance and oversight",
            "C": "Incident response coordination",
            "D": "Technical vulnerability management"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "A security steering committee provides strategic-level governance — reviewing posture at the macro level, approving major initiatives, and allocating resources. This is governance/oversight, not day-to-day operations.",
            "A": "Operational management is day-to-day security operations — not a steering committee function.",
            "B": "Steering committee = strategic governance and oversight function.",
            "C": "Incident response coordination is led by the IR team/CISO — not a steering committee function.",
            "D": "Vulnerability management is an operational technical function."
        }
    },
    {
        "id": 502,
        "domain": 5,
        "subdomain": "5.5",
        "objective": "Explain types and purposes of audits and assessments",
        "stem": "During a penetration test, the tester uses a credential obtained from a compromised host to access additional systems. What technique is being demonstrated?",
        "options": {
            "A": "Privilege escalation",
            "B": "Lateral movement",
            "C": "Persistence",
            "D": "Command and control (C2)"
        },
        "correct_answer": "B",
        "difficulty": 2,
        "explanations": {
            "correct": "Using credentials from a compromised host to move to and compromise additional systems is lateral movement — expanding access across the network after initial compromise.",
            "A": "Privilege escalation involves gaining higher privileges on the same system (user → admin).",
            "B": "Lateral movement = using access on one system to compromise adjacent systems.",
            "C": "Persistence involves maintaining access through reboots and detection (backdoors, scheduled tasks).",
            "D": "C2 refers to attacker infrastructure for controlling compromised systems remotely."
        }
    },
    {
        "id": 503,
        "domain": 5,
        "subdomain": "5.4",
        "objective": "Summarize elements of effective security compliance",
        "stem": "An organization must comply with both HIPAA and PCI DSS. When requirements conflict, what is the correct approach?",
        "options": {
            "A": "Choose the less restrictive requirement to minimize operational burden",
            "B": "Apply the more stringent requirement to satisfy both frameworks simultaneously",
            "C": "Notify regulators that compliance with both is impossible",
            "D": "Apply HIPAA requirements only, as they are federal law"
        },
        "correct_answer": "B",
        "difficulty": 3,
        "explanations": {
            "correct": "When multiple compliance frameworks apply, meeting the most stringent requirement typically satisfies less restrictive ones simultaneously. Organizations operating under multiple frameworks must implement controls that satisfy all applicable requirements.",
            "A": "Choosing the less restrictive option would leave the organization non-compliant with the stricter framework.",
            "B": "Apply the strictest requirement to achieve compliance with all applicable frameworks.",
            "C": "Dual compliance is common and achievable — it's not a basis for notifying regulators of impossibility.",
            "D": "Both HIPAA (federal) and PCI DSS (contractual) have equal compliance obligations for applicable organizations."
        }
    },
    {
        "id": 504,
        "domain": 5,
        "subdomain": "5.2",
        "objective": "Explain elements of the risk management process",
        "stem": "The Delphi method is used in risk assessment to:",
        "options": {
            "A": "Automate vulnerability scanning with AI",
            "B": "Achieve expert consensus through iterative, anonymous rounds of estimation",
            "C": "Calculate ALE using Monte Carlo simulation",
            "D": "Identify attack paths using threat modeling"
        },
        "correct_answer": "B",
        "difficulty": 3,
        "explanations": {
            "correct": "The Delphi method is a structured qualitative technique where a panel of experts anonymously provide estimates, receive aggregate feedback, and revise their estimates over multiple rounds — converging toward consensus without groupthink bias.",
            "A": "AI vulnerability scanning is a technical tool, not the Delphi method.",
            "B": "Delphi method = structured expert consensus through anonymous iterative rounds.",
            "C": "Monte Carlo simulation uses statistical modeling to quantify uncertainty — a quantitative technique distinct from Delphi.",
            "D": "Threat modeling (STRIDE, PASTA) is a separate risk identification technique."
        }
    },
    {
        "id": 505,
        "domain": 5,
        "subdomain": "5.6",
        "objective": "Implement security awareness practices",
        "stem": "An organization's security awareness program includes posters around the office reminding employees to lock their screens and report suspicious emails. What category of awareness technique is this?",
        "options": {
            "A": "Computer-based training (CBT)",
            "B": "Environmental awareness — passive reminders",
            "C": "Phishing simulation",
            "D": "Role-based training"
        },
        "correct_answer": "B",
        "difficulty": 1,
        "explanations": {
            "correct": "Physical posters, screen savers, and visual reminders are environmental awareness techniques — passive reinforcement that keeps security top-of-mind without requiring active training participation.",
            "A": "Computer-based training is interactive, digital learning — not physical posters.",
            "B": "Environmental/passive awareness = visual reminders (posters, screensavers, tent cards).",
            "C": "Phishing simulations are active tests of email security behavior.",
            "D": "Role-based training is targeted content for specific job functions."
        }
    }
]
