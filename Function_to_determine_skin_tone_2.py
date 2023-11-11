# Get user input
def get_user_input(prompt, options):
    while True:
        user_input = input(prompt).lower()
        if user_input in options:
            return user_input
        else:
            print("Invalid input. Please select from the given options.")

def determine_skin_tone():
    # Get user inputs for each parameter           
    sun_exposure = get_user_input("Enter your skin color (dark skin/red skin): ", ["dark skin", "red skin"])
    vessel_color = get_user_input("Enter the color of blood vessels in your wrist (green/purple): ", ["green", "purple"])
    skin_brightness = get_user_input("Enter the brightness of your skin compared to gold and silver (gold/silver): ", ["gold", "silver"])
    
    # Categorize sun exposure
    if sun_exposure == "dark skin":
        warm_score = 0.5
        cool_score = 0
        natural_score = 0.35
    elif sun_exposure == "red skin":
        warm_score = 0
        cool_score = 0.5
        natural_score = 0.35

    # Categorize vessel color
    if vessel_color == "green":
        warm_score += 0.5
        cool_score += 0
        natural_score += 0.35
    elif vessel_color == "purple":
        warm_score += 0
        cool_score += 0.5
        natural_score += 0.35

    # Categorize skin brightness
    if skin_brightness == "gold":
        warm_score += 0.5
        cool_score += 0
        natural_score += 0.35
    elif skin_brightness == "silver":
        warm_score += 0
        cool_score += 0.5
        natural_score += 0.35


    # Determine the final skin tone
    if warm_score > cool_score and warm_score > natural_score:
        return "Warm tones"
    elif cool_score > warm_score and cool_score > natural_score:
        return "Cool tones"
    else:
        return "Natural tones"


# Call the function to determine skin tone
skin_tone = determine_skin_tone()

# Display the result
print(f"The determined skin tone is {skin_tone}")

# Get user input style
def get_user_input_style(prompt, options):
    while True:
        user_input_style = input(prompt).strip().lower()  # Simplify by converting to lowercase in one line
        if user_input_style in options:
            return user_input_style
        else:
            print("Invalid input. Please select from the given options.")

def determine_style():
    # Get user inputs for each parameter           
    user_style = get_user_input_style("Enter your style that you want to know (Sporty/Street/Y2K/Preppy/Acubi/Minimal): ",
                                     ["sporty", "street", "y2k", "preppy", "acubi", "minimal"])  # Fixed typo in "preppy"

    if user_style == "sporty":
        return "การมิกซ์แอนด์แมตช์การแต่งตัวด้วยชุดกีฬา"
    elif user_style == "street":
        return "เน้นแต่งตัวในแบบที่สะท้อนความเป็นตัวเองมากที่สุดถือเป็นสไตล์ที่หยิบได้ทุกไอเท็มมาแมตช์ลุคได้อย่างอิสระ"
    elif user_style == "y2k":
        return "สไตล์แฟชั่นในช่วงปลายปี 90 จนถึงช่วงต้นของปี 2000 มีอย่างหลากหลาย ไม่ว่าจะเป็นเสื้อครอปท็อป เสื้อยืดสกรีนลายกราฟิก กางเกงเอวต่ำ เป็นต้น โดยเสื้อผ้าจะค่อนข้างฉูดฉาดเพื่อเน้นความสนุกในการแต่งตัว"
    elif user_style == "preppy":
        return "สไตล์ที่ได้รับแรงบันดาลใจมาจากเครื่องแบบนักศึกษา จุดเด่นคือการนำชุดลำลองและชุดกีฬามาสวมใส่"
    elif user_style == "acubi":
        return "สไตล์ที่หยิบยืมแนวคิดแบบ Minimalist หรือความเรียบง่ายมาใช้ และเสริมด้วยสไตล์ของ Cyber Fairy Grunge เข้ามา มักใช้โทนสีคลาสสิกเช่น ขาว, ดำ, เบจ และเทา"
    elif user_style == "minimal":
        return "เน้นการสไตล์ลิ่งไอเท็มต่างๆ ด้วยความเรียบง่าย โชว์ความน้อยแต่มากเรียบแต่โก้ และมักคุมด้วยโทนสีพื้น"
    else:
        return "Don't know"

# Call the function
style = determine_style()

# Display the function to explain style
print(f"คำอธิบายของสไตล์นี้คือ {style}")
