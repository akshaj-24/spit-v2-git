phase1 = {
  "phase": 1,
  "goals": [
    "Build rapport briefly and set the frame.",
    "Confirm consent to proceed."
  ],
  "topics": [
    "Name/pronouns preference (optional)",
    "Purpose + approximate structure/length",
    "Consent + comfort continuing",
    "Any immediate questions before starting"
  ],
  "optional_topics": [
    "Confidentiality limits (esp. safety), if your simulation benefits from it"
  ],
  "complete": [
    "Consent confirmed (yes/no recorded)",
    "Patient understands purpose/format (acknowledged)",
    "Patient had chance to ask initial questions (yes/no)"
  ],
  "instructions": """Warm and brief. Use mostly closed questions.
Allow at most one sentence of reassurance/validation.
Do not collect clinical history yet beyond a one-line reason for visit if the patient offers it spontaneously."""
}

phase2 = {
  "phase": 2,
  "goals": [
    "Elicit the main concerns in the patient’s words.",
    "Build a timeline and identify target symptoms and impairment."
  ],
  "topics": [
    "Main concern(s) and what prompted visit now",
    "Timeline: onset, course, recent change, triggers/precipitants",
    "Symptom deepening based on what emerges (mood/anxiety/trauma/psychosis/attention/sleep/appetite)",
    "Functional impact (work/school, relationships, self-care)",
    "Coping so far (helpful/unhelpful), prior help-seeking for this issue"
  ],
  "optional_topics": [
    "Patient goals/preferences for help"
  ],
  "complete": [
    "Top 1–3 presenting problems captured in patient language",
    "Timeline documented (onset + course + why-now trigger or ‘unclear’)",
    "At least 2 symptom clusters characterized (severity/frequency or examples)",
    "Functional impact characterized in at least 2 domains",
    "Patient’s goal for help stated (or explicitly unknown)"
  ],
  "instructions": """Start open-ended, then narrow with targeted follow-ups.
Ask for concrete examples (“What did that look like last week?”).
Avoid full diagnostic checklists; follow the signal from what the patient reports."""
}


phase3 = {
  "phase": 3,
  "goals": [
    "Identify background factors and recurring patterns relevant to the presenting problem."
  ],
  "topics": [
    "Prior episodes and prior treatment response",
    "Family/developmental context (brief, relevant only)",
    "Key relationships and supports",
    "Current stressors and life context",
    "Trauma/adversity screen only if clinically indicated and handled gently",
    "Strengths, values, protective factors"
  ],
  "optional_topics": [
    "Cultural/spiritual factors",
    "Identity factors relevant to care"
  ],
  "complete": [
    "Prior similar episodes assessed (yes/no + what helped)",
    "At least 1 key support and 1 key stressor identified",
    "At least 1 protective factor/strength identified",
    "Trauma/adversity addressed as ‘not asked / asked-denied / asked-endorsed’"
  ],
  "instructions": """Keep it relevant to the current concern. If the patient becomes distressed, slow down, validate, and pivot to stabilization/support questions."""
}


phase4 = {
  "phase": 4,
  "goals": [
    "Characterize safety and urgent clinical risks.",
    "Cover essential medical/substance/medication factors without derailing."
  ],
  "topics": [
    "Suicide/self-harm: ideation, intent, plan, means, timeframe, past attempts/NSSI, protective factors",
    "Harm to others (if indicated)",
    "Mania/hypomania screen (sleep/energy/risk-taking/pressured speech)",
    "Psychosis screen (hallucinations, delusions, paranoia)",
    "Substance use (alcohol, cannabis, stimulants, opioids, other) + recent changes",
    "Meds/supplements + adherence + side effects",
    "Brief medical flags (thyroid, sleep apnea, chronic pain, head injury) if relevant"
  ],
  "optional_topics": [
    "Access to lethal means (if SI present)"
  ],
  "complete": [
    "SI/NSSI assessed and documented as present/absent; if present, intent/plan/means/timeframe assessed",
    "Protective factors assessed (at least one, if any)",
    "Mania screen result documented (present/absent/unclear)",
    "Psychosis screen result documented (present/absent/unclear)",
    "Substance use characterized (at least alcohol/cannabis + one other category or ‘none’)",
    "Current meds captured (or explicitly none/unknown)"
  ],
  "instructions": """Be direct and calm. Use clear, non-leading questions.
If acute risk is endorsed, prioritize containment: clarify immediacy, means, supports, and willingness to stay safe before continuing."""
}


phase5 = {
  "phase": 5,
  "goals": [
    "Reflect an understandable model and confirm accuracy.",
    "Agree on next steps for care."
  ],
  "topics": [
    "Brief recap of main concerns + timeline + impact",
    "Tentative formulation (predisposing/precipitating/perpetuating/protective)",
    "Check accuracy and invite corrections",
    "Collaborative next steps"
  ],
  "optional_topics": [
    "Patient preferences (therapy, meds, lifestyle, support)"
  ],
  "complete": [
    "Interviewer summarizes and patient confirms or corrects key points",
    "At least 1 agreed next step stated",
    "Patient invited to add missing concerns"
  ],
  "instructions": """Use a short summary (3–6 sentences) then ask a single calibration question (“What did I miss?”).
Keep it collaborative and non-diagnostic unless the scenario requires it."""
}


phase6 = {
  "phase": 6,
  "goals": [
    "Close with clarity, support, and containment."
  ],
  "topics": [
    "Review next steps and logistics",
    "If any risk: simple safety plan (warning signs, coping steps, contacts, crisis resources)",
    "Final questions",
    "Thank and end"
  ],
  "optional_topics": [
    "Follow-up timeframe"
  ],
  "complete": [
    "Next steps restated clearly",
    "If risk present: safety steps documented (at least coping + contact)",
    "Patient has opportunity for final questions",
    "Session closed"
  ],
  "instructions": """Be concise, supportive, and practical. Avoid introducing new assessment domains unless needed for safety."""
}







# # Phase 1
# phase1 = {
#     "phase": 1,
#     "goals": [
#         "Introduce yourself and get to know the patient very briefly.",
#         "Explain the purpose of the session.",
#         "Obtain consent to proceed with the interview.",
#     ],
#     "topics": [
#         "Brief introduction",
#         "Format and length of this session",
#         "Consent confirmation (okay to continue)",
#         "Does patient have any questions before starting?",
#     ],
#     "optional_topics": [
        
#     ],
#     "complete": [
#         "Consent is confirmed",
#     ],
#     "instructions": """Use a warm, empathetic tone to build rapport and make the patient feel comfortable. Do not ask clinical specific questions in this phase. 
#     Try to keep it brief and to the point, minimize the number of questions you need to ask to complete this phase.
#     Use closed questions where possible to minimize patient burden adn restrict openness in this phase.""",
# }

# # Phase 2
# phase2 = {
#     "phase": 2,
#     "goals": [
#         "Understand why the patient is here, what changed, and what they want help with.",
#         "Build a coherent timeline and identify key symptoms/impairments.",
#     ],
#     "topics": [
#         "Presenting problem in the patient's own words",
#         "Timeline: onset, course, triggers/precipitants, recent changes",
#         "Symptom details: mood/anxiety/trauma/psychosis/attention/sleep/appetite, etc. (based on what emerges)",
#         "Functional impact: work/school, relationships, self-care, daily routines",
#         "Coping strategies used so far (helpful/unhelpful)",
#     ],
#     "optional_topics": [
#     ],
#     "complete": [
#         "You have a clear understanding of the presenting problem and what the patient is going through. You have a working hypothesis of the main problems and impacts.",
#     ],
#     "instructions": """Listen actively and empathetically. Use open-ended questions to explore the patient's concerns in their own words.
#     Use concise questions to not over burden the patient. Read through what you have already collected to avoid repeating questions.""",
# }

# # Phase 3
# phase3 = {
#     "phase": 3,
#     "goals": [
#         "Find contributing factors and patterns across the life course."
#     ],
#     "topics": [
#         "Developmental/childhood context (family environment, school, major stressors)",
#         "Prior similar episodes and what helped/didn’t",
#         "Significant relationships and attachment/support patterns",
#         "Recent life events (loss, conflict, moves, academic/work stress)",
#         "Trauma/adversity history (only if relevant and handled carefully)",
#         "Strengths, values, protective factors"
#     ],
#     "optional_topics": [
#         # Add any optional topics here if needed
#     ],
#     "complete": [
#         "You’ve captured the key background variables that plausibly relate to the presenting concern."
#     ],
#     "instructions": "Listen actively and empathetically. Use open-ended questions to explore the patient's concerns in their own words."
# }

# # Phase 4
# phase4 = {
#     "phase": 4,
#     "goals": [
#         "Ensure safety and rule out urgent conditions.",
#         "Fill essential gaps without derailing rapport."
#     ],
#     "topics": [
#         "Risk assessment: self-harm/suicidal ideation, intent/plan, past attempts, non-suicidal self-injury, protective factors; harm to others if indicated",
#         "Acute red flags as relevant: severe substance intoxication/withdrawal risk, mania/hypomania indicators, psychosis indicators",
#         "Substance use screen (basic)",
#         "Current meds/supplements, adherence, side effects (basic)",
#         "Medical factors that could affect symptoms (brief)"
#     ],
#     "optional_topics": [
#     ],
#     "complete": [
#         "Safety is reasonably characterized and any urgent concerns are either ruled out or clearly identified."
#     ],
#     "instructions": "Listen actively and empathetically. Use open-ended questions to explore the patient's concerns in their own words."
# }

# # Phase 6
# phase5 = {
#     "phase": 5,
#     "goals": [
#         "Reflect back an understandable model of what's going on.",
#         "Validate, check accuracy, and align on next steps."
#     ],
#     "topics": [
#         "Brief summary of key points",
#         "Tentative formulation (predisposing/precipitating/perpetuating/protective factors)",
#         "Ask: “Did I get that right?” “What feels most important that I missed?”"
#     ],
#     "optional_topics": [
#     ],
#     "complete": [
#         "Patient confirms understanding and accuracy, and you are aligned on next steps."
#     ],
#     "instructions": "Listen actively and empathetically. Use open-ended questions to explore the patient's concerns in their own words."
# }

# # Phase 7
# phase6 = {
#     "phase": 6,
#     "goals": [
#         "End with clarity and containment, not just 'more questions.'"
#     ],
#     "topics": [
#         "Next steps (e.g., coping strategies, therapy options, follow-up plan, resources)",
#         "If risk is present: a safety plan (even in simulation, you can include a simplified version)",
#         "Invite final questions",
#         "Thank and close session"
#     ],
#     "optional_topics": [
#     ],
#     "complete": [
#         "Next steps are clear, risk is addressed if present, and the session is closed with thanks."
#     ],
#     "instructions": "Listen actively and empathetically. Use open-ended questions to explore the patient's concerns in their own words."
# }


# Note format: SOAP
# This will be generated after the session ends based on review of the transcript and/or running summary.
summary = {
    "subjective": "The client’s self-reported symptoms, concerns, and reasons for the visit.",
    "objective": "Your observations, including the client’s demeanor and speech, risk assessment, and other parameters you deem fit.",
    "assessment": "Your clinical impressions, differential diagnoses, and any relevant formulations based on the information gathered.",
    "plan": "The next steps in treatment, such as interventions, assignments, or follow-ups.",
}