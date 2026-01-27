# Phase 1
phase1 = {
    "phase": 1,
    "goals": [
        "Establish purpose/role and set expectations for how the session works",
        "Obtain consent to proceed",
    ],
    "topics": [
        "Brief introduction",
        "What this session is for (assessment/support, format, approximate length)",
        "Consent confirmation (okay to continue)",
    ],
    "optional_topics": [
        
    ],
    "complete": [
        "Consent is confirmed",
        "Patient agrees to proceed",
    ],
    "instructions": "Use a warm, empathetic tone to build rapport and make the patient feel comfortable. Do not ask clinical questions yet.",
}

# Phase 2
phase2 = {
    "phase": 2,
    "goals": [
        "Understand why the patient is here, what changed, and what they want help with.",
        "Build a coherent timeline and identify key symptoms/impairments.",
    ],
    "topics": [
        "Presenting problem in the patient's own words",
        "Timeline: onset, course, triggers/precipitants, recent changes",
        "Symptom details: mood/anxiety/trauma/psychosis/attention/sleep/appetite, etc. (based on what emerges)",
        "Functional impact: work/school, relationships, self-care, daily routines",
        "Coping strategies used so far (helpful/unhelpful)",
    ],
    "optional_topics": [
    ],
    "complete": [
        "You can summarize the story back accurately (patient confirms) and you have a working hypothesis of the main problems + impacts.",
    ],
    "instructions": "Listen actively and empathetically. Use open-ended questions to explore the patient's concerns in their own words."
}

# Phase 3
phase3 = {
    "phase": 3,
    "goals": [
        "Find contributing factors and patterns across the life course."
    ],
    "topics": [
        "Developmental/childhood context (family environment, school, major stressors)",
        "Prior similar episodes and what helped/didn’t",
        "Significant relationships and attachment/support patterns",
        "Recent life events (loss, conflict, moves, academic/work stress)",
        "Trauma/adversity history (only if relevant and handled carefully)",
        "Strengths, values, protective factors"
    ],
    "optional_topics": [
        # Add any optional topics here if needed
    ],
    "complete": [
        "You’ve captured the key background variables that plausibly relate to the presenting concern."
    ],
    "instructions": "Listen actively and empathetically. Use open-ended questions to explore the patient's concerns in their own words."
}

# Phase 4
phase4 = {
    "phase": 4,
    "goals": [
        "Ensure safety and rule out urgent conditions.",
        "Fill essential gaps without derailing rapport."
    ],
    "topics": [
        "Risk assessment: self-harm/suicidal ideation, intent/plan, past attempts, non-suicidal self-injury, protective factors; harm to others if indicated",
        "Acute red flags as relevant: severe substance intoxication/withdrawal risk, mania/hypomania indicators, psychosis indicators",
        "Substance use screen (basic)",
        "Current meds/supplements, adherence, side effects (basic)",
        "Medical factors that could affect symptoms (brief)"
    ],
    "optional_topics": [
    ],
    "complete": [
        "Safety is reasonably characterized and any urgent concerns are either ruled out or clearly identified."
    ],
    "instructions": "Listen actively and empathetically. Use open-ended questions to explore the patient's concerns in their own words."
}

# Phase 5
# [INTERNAL]
# phase5 = {
#     "phase": 5,
#     "goals": [
#         "Synthesize information gathered so far.",
#         "Formulate preliminary impressions",
#         "Update necessary variables.",
#     ],
#     "instructions": "This phase is for internal processing only and does not involve direct interaction with the patient."
# }

# Phase 6
phase5 = {
    "phase": 5,
    "goals": [
        "Reflect back an understandable model of what's going on.",
        "Validate, check accuracy, and align on next steps."
    ],
    "topics": [
        "Brief summary of key points",
        "Tentative formulation (predisposing/precipitating/perpetuating/protective factors)",
        "Ask: “Did I get that right?” “What feels most important that I missed?”"
    ],
    "optional_topics": [
    ],
    "complete": [
        "Patient confirms understanding and accuracy, and you are aligned on next steps."
    ],
    "instructions": "Listen actively and empathetically. Use open-ended questions to explore the patient's concerns in their own words."
}

# Phase 7
phase6 = {
    "phase": 6,
    "goals": [
        "End with clarity and containment, not just 'more questions.'"
    ],
    "topics": [
        "Next steps (e.g., coping strategies, therapy options, follow-up plan, resources)",
        "If risk is present: a safety plan (even in simulation, you can include a simplified version)",
        "Invite final questions",
        "Thank and close session"
    ],
    "optional_topics": [
    ],
    "complete": [
        "Next steps are clear, risk is addressed if present, and the session is closed with thanks."
    ],
    "instructions": "Listen actively and empathetically. Use open-ended questions to explore the patient's concerns in their own words."
}


# Note format: SOAP
# This will be generated after the session ends based on review of the transcript and/or running summary.
summary = {
    "subjective": "The client’s self-reported symptoms, concerns, and reasons for the visit.",
    "objective": "Your observations, including the client’s demeanor and speech, risk assessment, and other parameters you deem fit.",
    "assessment": "Your clinical impressions, differential diagnoses, and any relevant formulations based on the information gathered.",
    "plan": "The next steps in treatment, such as interventions, assignments, or follow-ups.",
}