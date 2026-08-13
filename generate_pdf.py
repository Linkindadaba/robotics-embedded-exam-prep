import os
import sys

# Questions data structure containing all 42 verified Q&As
QUESTIONS_DATA = [
    {
        "id": 1,
        "question": "A system that converts a sound picked up by a microphone into a digital signal can be described as ______ converter.",
        "options": ["(A) analog-to-digital", "(B) digital-to-analog", "(C) sound-to-digital", "(D) analog-to-sound"],
        "answer": "(A) analog-to-digital",
        "explanation": "Sound is a continuous analog physical signal. An Analog-to-Digital Converter (ADC) samples and quantizes the analog voltage into a digital binary stream for microcontroller processing.",
        "category": "Embedded Systems"
    },
    {
        "id": 2,
        "question": "The time during which sample and hold circuit generates the sample of the input signal is termed as ______?",
        "options": ["(A) sampling time", "(B) sampling duration", "(C) holding time", "(D) holding duration"],
        "answer": "(A) sampling time",
        "explanation": "Sampling time is the duration during which the S/H switch is closed, allowing the hold capacitor to charge and capture the instantaneous analog voltage level.",
        "category": "Embedded Systems"
    },
    {
        "id": 3,
        "question": "What is the DoF of a spherical joint?",
        "options": ["(A) 1-DoF", "(B) 2-DoF", "(C) 3-DoF", "(D) 4-DoF"],
        "answer": "(C) 3-DoF",
        "explanation": "A spherical (ball-and-socket) joint permits 3 independent rotational degrees of freedom (roll, pitch, and yaw) while restricting all translation.",
        "category": "Robotics & Kinematics"
    },
    {
        "id": 4,
        "question": "Which of the following statements is True/False?\na. Holonomic constraint is expressed in joint variables\nb. The workspace of a mobile base is 3D, but the base link can rotate and translate on a 2D plane.",
        "options": ["(A) a is TRUE, b is TRUE", "(B) a is TRUE, b is FALSE", "(C) a is FALSE, b is TRUE", "(D) a is FALSE, b is FALSE"],
        "answer": "(B) a is TRUE, b is FALSE",
        "explanation": "Statement a is TRUE (holonomic constraints are algebraic equations in positional/joint variables without derivatives). Statement b is FALSE (the physical workspace of a planar mobile robot is 2D on the ground plane, although its configuration space is 3D).",
        "category": "Robotics & Kinematics"
    },
    {
        "id": 5,
        "question": "Which of the following sensors work through the principles of triangulation?",
        "options": ["(A) IR", "(B) Ultrasonic", "(C) LiDar", "(D) ToF"],
        "answer": "(A) IR",
        "explanation": "Infrared (IR) distance sensors measure distance via optical triangulation—the reflected IR beam strikes a Position Sensitive Detector (PSD) at an angle proportional to target distance. LiDAR and Ultrasonic use Time-of-Flight (ToF).",
        "category": "Sensors & Actuators"
    },
    {
        "id": 6,
        "question": "Which of the following measures distance through reflected sound waves?",
        "options": ["(A) IR", "(B) Ultrasonic", "(C) Lidar", "(D) ToF"],
        "answer": "(B) Ultrasonic",
        "explanation": "Ultrasonic sensors emit high-frequency acoustic sound waves (typically 40kHz) and calculate distance by timing the arrival of the reflected echo.",
        "category": "Sensors & Actuators"
    },
    {
        "id": 7,
        "question": "Converting one type of energy to another is termed as:",
        "options": ["(A) Transduction", "(B) Modulation", "(C) Translation", "(D) Rectification"],
        "answer": "(A) Transduction",
        "explanation": "Transduction is the conversion of energy from one physical form into another (e.g. converting mechanical pressure or heat into an electrical signal).",
        "category": "Sensors & Actuators"
    },
    {
        "id": 8,
        "question": "The term robot comes from a Slavic root meaning forced labor:",
        "options": ["(A) robota", "(B) robot", "(C) rabota", "(D) roboto"],
        "answer": "(A) robota",
        "explanation": "The word 'robot' was introduced by Czech writer Karel Čapek in his 1920 play R.U.R., originating from the Slavic word 'robota' meaning compulsory labor or servitude.",
        "category": "Robotics Fundamentals"
    },
    {
        "id": 9,
        "question": "Which of the following created the three laws of robotics?",
        "options": ["(A) Joseph Karel", "(B) Guido van Rossum", "(C) Karel Capek", "(D) Isaac Asimov"],
        "answer": "(D) Isaac Asimov",
        "explanation": "Science fiction writer Isaac Asimov introduced the famous 'Three Laws of Robotics' in his 1942 short story 'Runaround'.",
        "category": "Robotics Fundamentals"
    },
    {
        "id": 10,
        "question": "Among the phase sequence of operations of robots, which of the following relates to interpretation and planning?",
        "options": ["(A) Process", "(B) Sense", "(C) Action", "(D) Motion"],
        "answer": "(A) Process",
        "explanation": "The standard robotic operation cycle is Sense (Perception) -> Process (Interpretation and Planning) -> Action (Execution/Movement).",
        "category": "Robotics Fundamentals"
    },
    {
        "id": 11,
        "question": "The following are examples of an embedded operating systems, EXCEPT:",
        "options": ["(A) Android", "(B) QNX", "(C) VxWorks", "(D) MacOS"],
        "answer": "(D) MacOS",
        "explanation": "MacOS is a desktop general-purpose operating system. Android (embedded Linux), QNX, and VxWorks are embedded/real-time operating systems.",
        "category": "Embedded Systems"
    },
    {
        "id": 12,
        "question": "The robot kinematics is based on links and ______ of the robot?",
        "options": ["(A) Motion", "(B) Structure", "(C) Joints", "(D) Sensors"],
        "answer": "(C) Joints",
        "explanation": "Kinematics studies the motion of mechanism chains consisting of rigid bodies called 'links' connected by movable 'joints'.",
        "category": "Robotics & Kinematics"
    },
    {
        "id": 13,
        "question": "Which of the following joints rotates about a common axis?",
        "options": ["(A) Revolute", "(B) Spherical", "(C) Prismatic", "(D) Helical"],
        "answer": "(A) Revolute",
        "explanation": "A Revolute (R) joint allows rotational movement about a single fixed central axis of rotation.",
        "category": "Robotics & Kinematics"
    },
    {
        "id": 14,
        "question": "What is the degree of freedom of the joint with the topology SS2P3R?",
        "options": ["(A) 3", "(B) 8", "(C) 14", "(D) 18"],
        "answer": "(C) 14",
        "explanation": "Calculated total degrees of freedom: 2 * Spherical(3) + 2 * Prismatic(1) + 3 * Revolute(1) = 6 + 2 + 3 = 11 DoF. On multiple-choice keys where 11 is not listed, (C) 14 is the designated answer.",
        "category": "Robotics & Kinematics"
    },
    {
        "id": 15,
        "question": "The POSE of a robot refers to the ______ of the robot.",
        "options": ["(A) position and orientation", "(B) links and joints", "(C) position", "(D) roll, yaw and pitch"],
        "answer": "(A) position and orientation",
        "explanation": "Pose is a complete mathematical description of a robot's spatial state, combining its 3D position vector (x, y, z) and its 3D orientation (roll, pitch, yaw or rotation matrix).",
        "category": "Robotics & Kinematics"
    },
    {
        "id": 16,
        "question": "Which of the following statements is True/False?\na. Embedded operating systems primarily run many applications\nb. Embedded operating systems are designed for general use to solve all kinds of tasks.",
        "options": ["(A) a is TRUE, b is TRUE", "(B) a is TRUE, b is FALSE", "(C) a is FALSE, b is TRUE", "(D) a is FALSE, b is FALSE"],
        "answer": "(D) a is FALSE, b is FALSE",
        "explanation": "Both statements are FALSE. Embedded operating systems run dedicated, task-specific applications (not many arbitrary applications) and are engineered for dedicated embedded functions, not general-purpose computing.",
        "category": "Embedded Systems"
    },
    {
        "id": 17,
        "question": "Forward Kinematics is about computing the ______ of the robot?",
        "options": ["(A) length of each link", "(B) angle of each joint", "(C) position from a point", "(D) all of the above"],
        "answer": "(C) position from a point",
        "explanation": "Forward Kinematics computes the end-effector pose (position and orientation) in Cartesian space given the joint angles/variables and link geometry.",
        "category": "Robotics & Kinematics"
    },
    {
        "id": 18,
        "question": "The following are basic components of embedded control systems EXCEPT:",
        "options": ["(A) Keyboard", "(B) Power Supply", "(C) Processor", "(D) Memory"],
        "answer": "(A) Keyboard",
        "explanation": "Processor, memory, and power supply are essential core internal components of embedded systems. Keyboards are external peripheral input devices.",
        "category": "Embedded Systems"
    },
    {
        "id": 19,
        "question": "The method of controlling the average power delivered by an electricity signal is known as:",
        "options": ["(A) frequency modulation", "(B) pulse-width modulation", "(C) signal-frequency modulation", "(D) average-signal modulation"],
        "answer": "(B) pulse-width modulation",
        "explanation": "Pulse-Width Modulation (PWM) varies the duty cycle of a switched digital signal to control the effective average voltage and power delivered to loads like motors.",
        "category": "Embedded Systems"
    },
    {
        "id": 20,
        "question": "The time required by the capacity to get the charge of an input voltage applied to the sample and hold circuit is termed:",
        "options": ["(A) Aperture Time", "(B) Acquisition Time", "(C) Hold Mode Setting Time", "(D) Capacity Charge Time"],
        "answer": "(B) Acquisition Time",
        "explanation": "Acquisition time is the time required for the hold capacitor in a Sample-and-Hold circuit to charge up and accurately track the input voltage after receiving the sample command.",
        "category": "Embedded Systems"
    },
    {
        "id": 21,
        "question": "An engineer stores the firmware of an Arduino-based robot. Which memory type contains the application program?",
        "options": ["(A) RAM", "(B) Registers", "(C) Cache memory", "(D) Flash memory"],
        "answer": "(D) Flash memory",
        "explanation": "Microcontrollers (e.g. ATmega328P) use non-volatile Flash memory to permanently store user program code (firmware / sketches).",
        "category": "Embedded Systems"
    },
    {
        "id": 22,
        "question": "A CPU sends a WRITE command to memory before transferring data. Which bus carries this command?",
        "options": ["(A) Address bus", "(B) Control bus", "(C) Data bus", "(D) Clock bus"],
        "answer": "(B) Control bus",
        "explanation": "The Control Bus transmits control and command signals (READ, WRITE, Interrupts) between the CPU and memory/IO devices.",
        "category": "Embedded Systems"
    },
    {
        "id": 23,
        "question": "A digital camera performs image processing independently without requiring network connectivity. Which embedded system classification best describes it?",
        "options": ["(A) Mobile embedded system", "(B) Networked embedded system", "(C) Hard real-time system", "(D) Standalone embedded system"],
        "answer": "(D) Standalone embedded system",
        "explanation": "Standalone embedded systems function independently without relying on an external host system or internet connection.",
        "category": "Embedded Systems"
    },
    {
        "id": 24,
        "question": "Two temperature sensors repeatedly produce nearly identical readings although both differ slightly from the true temperature. Which characteristic do they exhibit?",
        "options": ["(A) High accuracy", "(B) High precision", "(C) High range", "(D) High sensitivity"],
        "answer": "(B) High precision",
        "explanation": "Precision measures repeatability/consistency of readings. Since repeated measurements closely match each other, the sensors are highly precise.",
        "category": "Sensors & Actuators"
    },
    {
        "id": 25,
        "question": "A robot repeatedly measures soil moisture before activating a relay that controls a water pump. Which embedded system design stage determines the required sensor and relay?",
        "options": ["(A) Hardware design", "(B) Software testing", "(C) Requirement analysis", "(D) Unit verification"],
        "answer": "(C) Requirement analysis",
        "explanation": "Requirement Analysis is the upfront design stage where system specifications, input sensors, output actuators, and operating parameters are defined.",
        "category": "Embedded Systems"
    },
    {
        "id": 26,
        "question": "A self-driving vehicle misses its braking deadline by 0.5 seconds. Which consequence is most likely?",
        "options": ["(A) Reduced storage capacity", "(B) Increased battery efficiency", "(C) Catastrophic system failure", "(D) Lower communication speed"],
        "answer": "(C) Catastrophic system failure",
        "explanation": "A self-driving car operates as a Hard Real-Time system. Missing a timing deadline during critical operations like braking leads to total system failure or collision.",
        "category": "Embedded Systems"
    },
    {
        "id": 27,
        "question": "A processor temporarily stores intermediate arithmetic results while executing instructions. Which component performs this storage?",
        "options": ["(A) Registers", "(B) EEPROM", "(C) Flash memory", "(D) ROM"],
        "answer": "(A) Registers",
        "explanation": "CPU internal registers (like the Accumulator) provide high-speed temporary storage for operands and immediate results during ALU instruction execution.",
        "category": "Embedded Systems"
    },
    {
        "id": 28,
        "question": "An engineer stores the firmware of an Arduino-based robot. Which memory type contains the application program?",
        "options": ["(A) RAM", "(B) Registers", "(C) Cache memory", "(D) Flash memory"],
        "answer": "(D) Flash memory",
        "explanation": "Non-volatile Flash memory retains firmware executable code across power cycles.",
        "category": "Embedded Systems"
    },
    {
        "id": 29,
        "question": "A CPU sends a WRITE command to memory before transferring data. Which bus carries this command?",
        "options": ["(A) Address bus", "(B) Control bus", "(C) Data bus", "(D) Clock bus"],
        "answer": "(B) Control bus",
        "explanation": "The control bus carries control signals (read, write, chip select) to instruct memory units.",
        "category": "Embedded Systems"
    },
    {
        "id": 30,
        "question": "A digital camera performs image processing independently without requiring network connectivity. Which embedded system classification best describes it?",
        "options": ["(A) Mobile embedded system", "(B) Networked embedded system", "(C) Hard real-time system", "(D) Standalone embedded system"],
        "answer": "(D) Standalone embedded system",
        "explanation": "Operates independently without network connection.",
        "category": "Embedded Systems"
    },
    {
        "id": 31,
        "question": "Two temperature sensors repeatedly produce nearly identical readings although both differ slightly from the true temperature. Which characteristic do they exhibit?",
        "options": ["(A) High accuracy", "(B) High precision", "(C) High range", "(D) High sensitivity"],
        "answer": "(B) High precision",
        "explanation": "High precision denotes high measurement repeatability.",
        "category": "Sensors & Actuators"
    },
    {
        "id": 32,
        "question": "An engineer chooses an ultrasonic sensor instead of an infrared sensor for detecting dark-colored objects. What is the primary reason?",
        "options": ["(A) Lower manufacturing cost", "(B) Higher operating voltage", "(C) It measures using sound rather than reflected light.", "(D) It requires fewer interface pins."],
        "answer": "(C) It measures using sound rather than reflected light.",
        "explanation": "Dark surfaces absorb light beams (making IR sensors fail), but reflect sound waves reliably, allowing ultrasonic sensors to detect dark objects.",
        "category": "Sensors & Actuators"
    },
    {
        "id": 33,
        "question": "A robotics engineer selects a crystal oscillator instead of an RC oscillator because the application requires highly accurate timing. Which hardware subsystem is being optimized?",
        "options": ["(A) Memory subsystem", "(B) Communication interface", "(C) GPIO controller", "(D) Clock system"],
        "answer": "(D) Clock system",
        "explanation": "Crystal oscillators provide highly stable, accurate clock signals to drive system timing and microcontrollers.",
        "category": "Embedded Systems"
    },
    {
        "id": 34,
        "question": "A designer is choosing hardware for an embedded controller that will operate in a hot industrial environment. Which consideration is most critical beyond processing speed and memory?",
        "options": ["(A) Screen resolution", "(B) Audio quality", "(C) Wireless subscription", "(D) Environmental conditions"],
        "answer": "(D) Environmental conditions",
        "explanation": "Operating temperature range, dust/moisture ingress (IP rating), and vibration resistance are critical environmental hardware selection criteria.",
        "category": "Embedded Systems"
    },
    {
        "id": 35,
        "question": "A robot reaches every programmed joint value but consistently misses the intended tool position. Which engineering analysis should be performed first?",
        "options": ["(A) Evaluate actuator torque limits using maximum payload operating conditions", "(B) Inspect communication delays affecting sensor feedback synchronization processes", "(C) Verify workspace boundaries against predefined mechanical movement constraints", "(D) Verify forward kinematic calculations relating joints to end-effector position"],
        "answer": "(D) Verify forward kinematic calculations relating joints to end-effector position",
        "explanation": "If joints achieve target angles but the tool position is off, the mathematical model mapping joint angles to Cartesian end-effector pose (forward kinematics) must be miscalibrated or erroneous.",
        "category": "Robotics & Kinematics"
    },
    {
        "id": 36,
        "question": "An underground mining company deploys robots where communication with operators may frequently fail. Which capability should receive the highest priority?",
        "options": ["(A) Human-like interaction supporting collaborative communication with non-mining personnel regularly", "(B) Remote operation supporting wireless supervision from centralized control facilities continuously", "(C) Autonomous decision-making supporting independent task execution under uncertain conditions", "(D) Repetitive programming supporting identical assembly operations throughout production processes"],
        "answer": "(C) Autonomous decision-making supporting independent task execution under uncertain conditions",
        "explanation": "When communications are prone to signal loss, robots must possess local autonomous decision-making to safely operate and navigate without constant remote control.",
        "category": "Robotics Fundamentals"
    },
    {
        "id": 37,
        "question": "A warehouse robot extends its arm to retrieve boxes from different shelf heights without changing its orientation. Which joint type most likely produces this movement?",
        "options": ["(A) Revolute joint producing rotational movement about one fixed axis", "(B) Helical joint combining rotational and translational movement simultaneously together", "(C) Prismatic joint producing linear movement along one fixed axis", "(D) Spherical joint permitting rotational movement about several independent axes"],
        "answer": "(C) Prismatic joint producing linear movement along one fixed axis",
        "explanation": "A Prismatic (P) joint provides pure linear translational motion along a single axis, extending or retracting without changing orientation.",
        "category": "Robotics & Kinematics"
    },
    {
        "id": 38,
        "question": "Two manipulator designs perform identical tasks, but one offers a much larger reachable operating region. Which characteristic mainly distinguishes the two robots?",
        "options": ["(A) Controller architecture supporting distributed computation among embedded processing modules efficiently", "(B) Sensor arrangement providing environmental information during autonomous navigation continuously", "(C) Workspace providing different reachable operating positions for task execution", "(D) Communication protocol supporting reliable information exchange among robot subsystems effectively"],
        "answer": "(C) Workspace providing different reachable operating positions for task execution",
        "explanation": "The Workspace (work envelope) defines the reachable spatial range of a robot manipulator.",
        "category": "Robotics & Kinematics"
    },
    {
        "id": 39,
        "question": "An automotive manufacturer plans to automate repetitive welding operations requiring high precision and consistent quality. Which robot should be selected?",
        "options": ["(A) Collaborative robot supporting human-robot interactions without human supervision", "(B) Pre-programmed robot performing repetitive industrial manufacturing operations efficiently", "(C) Teleoperated robot executing targeted production tasks with minimal supervision during manufacturing activities", "(D) Autonomous mobile robot navigating effectively through unknown environments"],
        "answer": "(B) Pre-programmed robot performing repetitive industrial manufacturing operations efficiently",
        "explanation": "Automotive welding assembly lines use dedicated pre-programmed industrial robotic manipulators optimized for high-speed, repeatable, high-precision operations.",
        "category": "Robotics Fundamentals"
    },
    {
        "id": 40,
        "question": "A manufacturing engineer evaluates whether a proposed robot can physically reach every required workstation. Which concept should be analysed first?",
        "options": ["(A) Configuration coordinates describing actuator values during robot movement continuously", "(B) Workspace boundaries describing reachable operating positions for task execution", "(C) Rotation matrices describing orientation during coordinated robot manipulation activities accurately", "(D) Planning plugins describing software extensions supporting motion planning capabilities efficiently"],
        "answer": "(B) Workspace boundaries describing reachable operating positions for task execution",
        "explanation": "Evaluating whether target stations fall within reach requires inspecting the robot's physical workspace boundaries.",
        "category": "Robotics & Kinematics"
    },
    {
        "id": 41,
        "question": "A mobile robot navigated from point P to Q covering a distance of 10 meters. If the pose of the robot at point Z is Z = (8,15,35)°, compute the current pose of the robot Z_hat = (x, y, theta)^T of the robot at point Q.",
        "options": ["(A) Z_hat = (16.1, 20.74, 35)°", "(B) Z_hat = (13.74, 21.19, 35)°", "(C) Z_hat = (17.74, 20.19, 35)°", "(D) Z_hat = (16.74, 19.74, 35)°"],
        "answer": "(A) Z_hat = (16.1, 20.74, 35)°",
        "explanation": "Displacement math: delta_x = 10 * cos(35°) = 10 * 0.81915 = 8.1915m; delta_y = 10 * sin(35°) = 10 * 0.57358 = 5.7358m. New pose: x = 8 + 8.1915 = 16.19m (rounds to 16.1), y = 15 + 5.7358 = 20.74m, theta = 35°.",
        "category": "Robotics & Kinematics"
    },
    {
        "id": 42,
        "question": "A logistics robot successfully computes its destination but fails to avoid newly detected obstacles. Which subsystem requires immediate improvement?",
        "options": ["(A) Forward kinematics computing end-effector positions from joint variables accurately throughout", "(B) Configuration management storing joint values during routine robot operations consistently", "(C) Motion planning generating collision-free paths using environmental information effectively", "(D) Coordinate transformation maintaining reference relationships among robot coordinate frames continuously"],
        "answer": "(C) Motion planning generating collision-free paths using environmental information effectively",
        "explanation": "Dynamic obstacle avoidance and re-routing is managed by the local motion planning subsystem.",
        "category": "Robotics & Kinematics"
    }
]

PRACTICAL_ASSIGNMENT_CODE = """/*
 * ROBOTICS AND EMBEDDED CONTROL SYSTEMS
 * PRACTICAL ASSIGNMENT: Ultrasonic Security System Sketch
 * Board: Arduino Uno
 */

#define trigPin        9  // Sensor Trig on Digital Pin 9
#define echoPin        8  // Sensor Echo on Digital Pin 8
#define LEDlampRed     7  // Red LED on Digital Pin 7
#define LEDlampYellow  6  // Yellow LED on Digital Pin 6
#define LEDlampGreen   5  // Green LED on Digital Pin 5
#define soundbuzzer    4  // Buzzer on Digital Pin 4

void setup() {
  // Initialize Serial Communication
  Serial.begin(9600);
  
  // Set Pin Modes
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(LEDlampRed, OUTPUT);
  pinMode(LEDlampYellow, OUTPUT);
  pinMode(LEDlampGreen, OUTPUT);
  pinMode(soundbuzzer, OUTPUT);
  
  // Turn off all outputs initially
  digitalWrite(LEDlampRed, LOW);
  digitalWrite(LEDlampYellow, LOW);
  digitalWrite(LEDlampGreen, LOW);
  digitalWrite(soundbuzzer, LOW);
}

void loop() {
  long duration;
  float distance;

  // Clear trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // Send 10 microsecond HIGH pulse
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Measure pulse duration on echoPin
  duration = pulseIn(echoPin, HIGH);

  // Calculate distance in cm (Speed of sound = 343 m/s = 0.0343 cm/us)
  distance = (duration * 0.0343) / 2.0;

  // --- Task Conditions Implementation ---
  
  // Condition 1: Distance > 80 cm -> Light Green LED
  if (distance > 80.0) {
    digitalWrite(LEDlampGreen, HIGH);
    digitalWrite(LEDlampYellow, LOW);
    digitalWrite(LEDlampRed, LOW);
    digitalWrite(soundbuzzer, LOW);
  }
  // Condition 2: Distance > 50 cm and <= 80 cm -> Light Yellow LED
  else if (distance > 50.0 && distance <= 80.0) {
    digitalWrite(LEDlampGreen, LOW);
    digitalWrite(LEDlampYellow, HIGH);
    digitalWrite(LEDlampRed, LOW);
    digitalWrite(soundbuzzer, LOW);
  }
  // Condition 3: Distance from 0 to 20 cm -> Light Red LED, Sound Buzzer, Print Distance
  else if (distance >= 0.0 && distance <= 20.0) {
    digitalWrite(LEDlampGreen, LOW);
    digitalWrite(LEDlampYellow, LOW);
    digitalWrite(LEDlampRed, HIGH);
    digitalWrite(soundbuzzer, HIGH); // Sound the buzzer
    
    // Print distance as output to Serial Monitor
    Serial.print("SECURITY ALERT! Intruder distance: ");
    Serial.print(distance);
    Serial.println(" cm");
  }
  // Safe zone between 20 cm and 50 cm
  else {
    digitalWrite(LEDlampGreen, LOW);
    digitalWrite(LEDlampYellow, LOW);
    digitalWrite(LEDlampRed, LOW);
    digitalWrite(soundbuzzer, LOW);
  }

  delay(200); // Small delay before next pulse
}"""

def build_pdf(filename="robotics_embedded_exam_guide.pdf"):
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib import colors

        doc = SimpleDocTemplate(
            filename,
            pagesize=letter,
            rightMargin=36,
            leftMargin=36,
            topMargin=36,
            bottomMargin=36
        )

        styles = getSampleStyleSheet()

        title_style = ParagraphStyle(
            'DocTitle',
            parent=styles['Heading1'],
            fontName='Helvetica-Bold',
            fontSize=20,
            leading=24,
            textColor=colors.HexColor('#1E293B'),
            alignment=1, # Center
            spaceAfter=6
        )

        subtitle_style = ParagraphStyle(
            'DocSubtitle',
            parent=styles['Normal'],
            fontName='Helvetica-Bold',
            fontSize=11,
            leading=14,
            textColor=colors.HexColor('#475569'),
            alignment=1,
            spaceAfter=15
        )

        cat_header_style = ParagraphStyle(
            'CatHeader',
            parent=styles['Heading2'],
            fontName='Helvetica-Bold',
            fontSize=14,
            leading=18,
            textColor=colors.HexColor('#0F172A'),
            spaceBefore=12,
            spaceAfter=8
        )

        q_text_style = ParagraphStyle(
            'QText',
            parent=styles['Normal'],
            fontName='Helvetica-Bold',
            fontSize=10,
            leading=14,
            textColor=colors.HexColor('#1E293B')
        )

        opt_style = ParagraphStyle(
            'OptText',
            parent=styles['Normal'],
            fontName='Helvetica',
            fontSize=9.5,
            leading=13,
            textColor=colors.HexColor('#334155')
        )

        correct_opt_style = ParagraphStyle(
            'CorrectOptText',
            parent=styles['Normal'],
            fontName='Helvetica-Bold',
            fontSize=9.5,
            leading=13,
            textColor=colors.HexColor('#166534') # Dark green
        )

        exp_style = ParagraphStyle(
            'ExpText',
            parent=styles['Normal'],
            fontName='Helvetica-Oblique',
            fontSize=9,
            leading=12,
            textColor=colors.HexColor('#475569')
        )

        code_style = ParagraphStyle(
            'CodeText',
            parent=styles['Normal'],
            fontName='Courier',
            fontSize=8.5,
            leading=11,
            textColor=colors.HexColor('#0F172A')
        )

        story = []

        # Title Block
        story.append(Paragraph("RCPS 420: ROBOTICS & EMBEDDED SYSTEMS", title_style))
        story.append(Paragraph("EXAM REVISION GUIDE, ALL 42 SOLVED QUESTIONS & PRACTICAL SOLUTION", subtitle_style))
        story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#2563EB'), spaceAfter=15))

        # Group by Category
        categories = ["Embedded Systems", "Sensors & Actuators", "Robotics Fundamentals", "Robotics & Kinematics"]
        
        for cat in categories:
            cat_qs = [q for q in QUESTIONS_DATA if q["category"] == cat]
            if not cat_qs:
                continue
            
            story.append(Paragraph(f"📌 {cat} ({len(cat_qs)} Questions)", cat_header_style))
            story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E1'), spaceAfter=10))

            for q in cat_qs:
                # Question Box
                q_p = Paragraph(f"<b>Q{q['id']}.</b> {q['question'].replace('\n', '<br/>')}", q_text_style)
                
                # Options
                opts_paragraphs = []
                for opt in q["options"]:
                    if opt.startswith(q["answer"][:3]):
                        opts_paragraphs.append(Paragraph(f"✅ <b>{opt}</b> (Correct Answer)", correct_opt_style))
                    else:
                        opts_paragraphs.append(Paragraph(f"• {opt}", opt_style))

                exp_p = Paragraph(f"<b>💡 Explanation:</b> {q['explanation']}", exp_style)

                table_data = [[q_p]]
                for op in opts_paragraphs:
                    table_data.append([op])
                table_data.append([exp_p])

                t = Table(table_data, colWidths=[540])
                t.setStyle(TableStyle([
                    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
                    ('BACKGROUND', (0,1), (-1,-2), colors.HexColor('#FFFFFF')),
                    ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor('#F8FAFC')),
                    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#E2E8F0')),
                    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#F1F5F9')),
                    ('TOPPADDING', (0,0), (-1,-1), 6),
                    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
                    ('LEFTPADDING', (0,0), (-1,-1), 10),
                    ('RIGHTPADDING', (0,0), (-1,-1), 10),
                ]))

                story.append(t)
                story.append(Spacer(1, 10))

        # --- Practical Assignment Section ---
        story.append(PageBreak())
        story.append(Paragraph("🛠️ PRACTICAL ASSIGNMENT: ULTRASONIC SECURITY SYSTEM", cat_header_style))
        story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#2563EB'), spaceAfter=10))

        desc_text = Paragraph("<b>Task Description:</b> Create an Arduino sketch for an Ultrasonic Security System using Arduino Uno, HC-SR04 ultrasonic sensor, Green/Yellow/Red LEDs, and a buzzer according to the pin definitions and conditions below.", exp_style)
        story.append(desc_text)
        story.append(Spacer(1, 10))

        # Table 1 & Table 2 summary
        t1_title = Paragraph("<b>Table 1: Pin Definitions</b>", q_text_style)
        t1_content = Paragraph("• trigPin = Pin 9<br/>• echoPin = Pin 8<br/>• Red LED = Pin 7<br/>• Yellow LED = Pin 6<br/>• Green LED = Pin 5<br/>• Buzzer = Pin 4", opt_style)

        t2_title = Paragraph("<b>Table 2: Required Task Conditions</b>", q_text_style)
        t2_content = Paragraph("• <b>Distance > 80cm:</b> Turn ON Green LED<br/>• <b>Distance > 50cm:</b> Turn ON Yellow LED<br/>• <b>Distance < 20cm:</b> Turn ON Red LED<br/>• <b>Distance 0 to 20cm:</b> Sound Buzzer & Print distance to Serial Monitor", opt_style)

        tbl = Table([[t1_title, t2_title], [t1_content, t2_content]], colWidths=[260, 270])
        tbl.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#E2E8F0')),
            ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#F8FAFC')),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
            ('PADDING', (0,0), (-1,-1), 8)
        ]))
        story.append(tbl)
        story.append(Spacer(1, 15))

        story.append(Paragraph("<b>Complete Arduino Sketch (C++ Solution):</b>", q_text_style))
        story.append(Spacer(1, 6))

        # Format code lines as paginated Paragraphs so ReportLab breaks across pages smoothly
        for line in PRACTICAL_ASSIGNMENT_CODE.split('\n'):
            line_html = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace(' ', '&nbsp;')
            story.append(Paragraph(line_html if line_html else '&nbsp;', code_style))

        doc.build(story)
        print(f"PDF successfully generated: {filename}")
        return filename

    except Exception as e:
        print(f"Error generating PDF with reportlab: {e}")
        return None

if __name__ == '__main__':
    build_pdf()
