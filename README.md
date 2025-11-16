NIRBHAYA – LoRa-Based Child Safety & Fall Detection Ecosystem

Nirbhaya is an always-connected child safety ecosystem designed to provide continuous tracking, motion detection, and tamper alerts even in dead zones, basements, rural areas, and indoors where GPS and mobile networks fail.

It uses: LoRa Peer-to-Peer (865 MHz) for long-range communication
Arduino Nano as the low-power core
MPU-6050 for fall and abnormal-motion detection
Parent-side mobile app & LoRa gateway

This system provides unbreakable peace of mind to parents and ensures that children remain safe and trackable everywhere.

🎯 Problem Statement

Traditional trackers fail when they are needed the most:

❌ GPS goes blind indoors
❌ Mobile networks have dead zones (parks, basements, schools)
❌ Bluetooth trackers have <30m range
❌ High subscription costs
❌ Easily tampered devices

Every 8 minutes a child goes missing in India. Existing solutions offer partial protection, not reliability.

🚀 Our Solution: Nirbhaya Ecosystem A complete hardware–software safety ecosystem that uses LoRa P2P communication (no SIM, no GPS) to ensure continuous operation everywhere.

Core Benefits
Works even without mobile network or GPS
Up to 8 km LoRa coverage
Fall detection + abnormal-motion alerts
Zero subscription fees
Reliable tracking indoors + outdoors

🛠️ Tech Stack
Hardware
Component	Purpose
Arduino Nano	Low-power central processor
LoRa SX1278 (865 MHz)	Long-range P2P communication
MPU-6050	Motion, fall, and acceleration detection
Software

📡 System Architecture
+-------------------+          LoRa P2P           +---------------------+
| Child Device      | <-------------------------> | Parent LoRa Gateway |
| (Wristband)       |                             | (Home/School Unit)  |
+-------------------+                             +----------+----------+
         |                                                    |
         | Motion/Fall Alerts                                 |
         |                                                    v
         |                                        +---------------------+
         |                                        | Parent Mobile App   |
         +--------------------------------------> | Notifications, UI   |
                                                  +---------------------+

📲 Key Features
1. Always-On LoRa Network

Works even in:
Schools
Rural areas
Indoors
Basements
Public parks

No GPS = no blind spots.
No SIM = no monthly fees.

2. Fall Detection (MPU-6050)
Real-time fall detection
Sudden impact recognition
Unusual-activity alerts
Configurable thresholds in firmware

🔧 How It Works (Process Flow)
[Child Moves]  
     |
     v
[MPU-6050 Detects Motion/Fall]
     |
     v
[Arduino Processes the Event]
     |
     v
[LoRa Transmits Alert (865 MHz)]
     |
     v
[Parent Gateway Receives Signal]
     |
     v
[Web App Sends Notification]

📅 Implementation Plan
Phase 1: Research & Design — Completed
Validated market
Designed LoRa P2P architecture
65% waitlist confirmation

Phase 2: Development — 🔄 In Progress
Firmware optimization
Enclosure design
Parent app UI/UX

Hardware Setup
Connect LoRa SX1278 to Arduino Nano
Connect MPU-6050 via I²C
Flash firmware via Arduino IDE

Done 🚀

📈 Impact & Benefits
Economic Impact

Saves ₹1,000–₹2,000 yearly (no subscription fees)
Targeting $1M SAM, growing to $3.3M by 2033
Social Impact
Protects children
Gives parents confidence
Enables girls’ education & safety
Helps the specially-abled & dementia patients
Who Benefits?

Parents in Tier-1 & Tier-2 cities
Schools, institutions
Healthcare (Alzheimer’s monitoring)
🧪 Validation
200+ parent survey
90% purchase intent
Pilot secured with 2 major residential communities

👨‍💻 Team

Sumith Subraya Nayak – Tech Development
H M Brunda – Hardware & Firmware
Sathya M – Product Analyst & QA
Karan S – Project Management


🏁 Conclusion
Nirbhaya is more than a tracker — it’s a lifesaving ecosystem.
It ensures that every child can explore, play, and grow with fearless curiosity.
