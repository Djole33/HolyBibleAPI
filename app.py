# Import Flask library for creating web applications
from flask import Flask, jsonify, request
import os

# Initialize Flask application
app = Flask(__name__)
port = int(os.getenv('PORT', 4000))

# List of Bible verses
bible_verses = [
    {"id": 1, "verse": "Let there be light", "book": "Genesis 1:3"},
    {"id": 2, "verse": "For I know the plans I have for you, declares the Lord, plans for welfare and not for evil, to give you a future and a hope.", "book": "Jeremiah 29:11"},
    {"id": 3, "verse": "I can do all things through him who strengthens me.", "book": "Philippians 4:13"},
    {"id": 4, "verse": "The Lord is my shepherd; I shall not want.", "book": "Psalm 23:1"},
    {"id": 5, "verse": "In the beginning, God created the heavens and the earth.", "book": "Genesis 1:1"},
    {"id": 6, "verse": "For God so loved the world, that he gave his only Son, that whoever believes in him should not perish but have eternal life.", "book": "John 3:16"},
    {"id": 7, "verse": "But the fruit of the Spirit is love, joy, peace, patience, kindness, goodness, faithfulness, gentleness, self-control; against such things there is no law.", "book": "Galatians 5:22-23"},
    {"id": 8, "verse": "And we know that for those who love God all things work together for good, for those who are called according to his purpose.", "book": "Romans 8:28"},
    {"id": 9, "verse": "The Lord bless you and keep you; the Lord make his face to shine upon you and be gracious to you; the Lord lift up his countenance upon you and give you peace.", "book": "Numbers 6:24-26"},
    {"id": 10, "verse": "I have been crucified with Christ. It is no longer I who live, but Christ who lives in me. And the life I now live in the flesh I live by faith in the Son of God, who loved me and gave himself for me.", "book": "Galatians 2:20"},
    {"id": 11, "verse": "For by grace you have been saved through faith. And this is not your own doing; it is the gift of God, not a result of works, so that no one may boast.", "book": "Ephesians 2:8-9"},
    {"id": 12, "verse": "The steadfast love of the Lord never ceases; his mercies never come to an end; they are new every morning; great is your faithfulness.", "book": "Lamentations 3:22-23"},
    {"id": 13, "verse": "Jesus said to him, 'I am the way, and the truth, and the life. No one comes to the Father except through me.'", "book": "John 14:6"},
    {"id": 14, "verse": "But they who wait for the Lord shall renew their strength; they shall mount up with wings like eagles; they shall run and not be weary; they shall walk and not faint.", "book": "Isaiah 40:31"},
    {"id": 15, "verse": "The Lord is my light and my salvation; whom shall I fear? The Lord is the stronghold of my life; of whom shall I be afraid?", "book": "Psalm 27:1"},
    {"id": 16, "verse": "For the wages of sin is death, but the free gift of God is eternal life in Christ Jesus our Lord.", "book": "Romans 6:23"},
    {"id": 17, "verse": "Do not be anxious about anything, but in everything by prayer and supplication with thanksgiving let your requests be made known to God.", "book": "Philippians 4:6"},
    {"id": 18, "verse": "Trust in the Lord with all your heart, and do not lean on your own understanding. In all your ways acknowledge him, and he will make straight your paths.", "book": "Proverbs 3:5-6"},
    {"id": 19, "verse": "The Lord is near to the brokenhearted and saves the crushed in spirit.", "book": "Psalm 34:18"},
    {"id": 20, "verse": "But God shows his love for us in that while we were still sinners, Christ died for us.", "book": "Romans 5:8"},
    {"id": 21, "verse": "In my distress I called to the Lord, and he answered me.", "book": "Psalm 120:1"},
    {"id": 22, "verse": "Rejoice in the Lord always; again I will say, rejoice.", "book": "Philippians 4:4"},
    {"id": 23, "verse": "And he said to me, 'My grace is sufficient for you, for my power is made perfect in weakness.' Therefore I will boast all the more gladly of my weaknesses, so that the power of Christ may rest upon me.", "book": "2 Corinthians 12:9"},
    {"id": 24, "verse": "For God gave us a spirit not of fear but of power and love and self-control.", "book": "2 Timothy 1:7"},
    {"id": 25, "verse": "But seek first the kingdom of God and his righteousness, and all these things will be added to you.", "book": "Matthew 6:33"},
    {"id": 26, "verse": "And Jesus came and said to them, 'All authority in heaven and on earth has been given to me. Go therefore and make disciples of all nations, baptizing them in the name of the Father and of the Son and of the Holy Spirit.'", "book": "Matthew 28:18-19"},
    {"id": 27, "verse": "Come to me, all who labor and are heavy laden, and I will give you rest.", "book": "Matthew 11:28"},
    {"id": 28, "verse": "I have told you these things, so that in me you may have peace. In this world you will have trouble. But take heart! I have overcome the world.", "book": "John 16:33"},
    {"id": 29, "verse": "The thief comes only to steal and kill and destroy. I came that they may have life and have it abundantly.", "book": "John 10:10"},
    {"id": 30, "verse": "Be strong and courageous. Do not be frightened, and do not be dismayed, for the Lord your God is with you wherever you go.", "book": "Joshua 1:9"},
    {"id": 31, "verse": "Therefore, if anyone is in Christ, he is a new creation. The old has passed away; behold, the new has come.", "book": "2 Corinthians 5:17"},
    {"id": 32, "verse": "The fear of the Lord is the beginning of knowledge; fools despise wisdom and instruction.", "book": "Proverbs 1:7"},
    {"id": 33, "verse": "And the peace of God, which surpasses all understanding, will guard your hearts and your minds in Christ Jesus.", "book": "Philippians 4:7"},
    {"id": 34, "verse": "For where two or three are gathered in my name, there am I among them.", "book": "Matthew 18:20"},
    {"id": 35, "verse": "And let us not grow weary of doing good, for in due season we will reap, if we do not give up.", "book": "Galatians 6:9"},
    {"id": 36, "verse": "No temptation has overtaken you that is not common to man. God is faithful, and he will not let you be tempted beyond your ability, but with the temptation he will also provide the way of escape, that you may be able to endure it.", "book": "1 Corinthians 10:13"},
    {"id": 37, "verse": "You will keep in perfect peace those whose minds are steadfast, because they trust in you.", "book": "Isaiah 26:3"},
    {"id": 38, "verse": "For the word of God is alive and active. Sharper than any double-edged sword, it penetrates even to dividing soul and spirit, joints and marrow; it judges the thoughts and attitudes of the heart.", "book": "Hebrews 4:12"},
    {"id": 39, "verse": "So faith comes from hearing, and hearing through the word of Christ.", "book": "Romans 10:17"},
    {"id": 40, "verse": "But the Lord is faithful. He will establish you and guard you against the evil one.", "book": "2 Thessalonians 3:3"},
    {"id": 41, "verse": "Whoever has my commands and keeps them is the one who loves me. The one who loves me will be loved by my Father, and I too will love them and show myself to them.", "book": "John 14:21"},
    {"id": 42, "verse": "If any of you lacks wisdom, let him ask of God, who gives to all liberally and without reproach, and it will be given to him.", "book": "James 1:5"},
    {"id": 43, "verse": "And now these three remain: faith, hope, and love. But the greatest of these is love.", "book": "1 Corinthians 13:13"},
    {"id": 44, "verse": "Cast all your anxiety on him because he cares for you.", "book": "1 Peter 5:7"},
    {"id": 45, "verse": "And he has said to me, 'My grace is sufficient for you, for power is perfected in weakness.' Most gladly, therefore, I will rather boast about my weaknesses, so that the power of Christ may dwell in me.", "book": "2 Corinthians 12:9"},
    {"id": 46, "verse": "I am the Alpha and the Omega, the First and the Last, the Beginning and the End.", "book": "Revelation 22:13"},
    {"id": 47, "verse": "And without faith it is impossible to please him, for whoever would draw near to God must believe that he exists and that he rewards those who seek him.", "book": "Hebrews 11:6"},
    {"id": 48, "verse": "For we live by faith, not by sight.", "book": "2 Corinthians 5:7"},
    {"id": 49, "verse": "But in your hearts honor Christ the Lord as holy, always being prepared to make a defense to anyone who asks you for a reason for the hope that is in you; yet do it with gentleness and respect.", "book": "1 Peter 3:15"},
    {"id": 50, "verse": "Create in me a clean heart, O God, and renew a right spirit within me.", "book": "Psalm 51:10"},
    {"id": 51, "verse": "Blessed is the man who remains steadfast under trial, for when he has stood the test he will receive the crown of life, which God has promised to those who love him.", "book": "James 1:12"},
    {"id": 52, "verse": "He who dwells in the shelter of the Most High will rest in the shadow of the Almighty.", "book": "Psalm 91:1"},
    {"id": 53, "verse": "Therefore, if anyone is in Christ, he is a new creation. The old has passed away; behold, the new has come.", "book": "2 Corinthians 5:17"},
    {"id": 54, "verse": "For I am convinced that neither death nor life, neither angels nor demons, neither the present nor the future, nor any powers, neither height nor depth, nor anything else in all creation, will be able to separate us from the love of God that is in Christ Jesus our Lord.", "book": "Romans 8:38-39"},
    {"id": 55, "verse": "So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand.", "book": "Isaiah 41:10"},
    {"id": 56, "verse": "I have hidden your word in my heart that I might not sin against you.", "book": "Psalm 119:11"},
    {"id": 57, "verse": "Give thanks to the Lord, for he is good; his love endures forever.", "book": "Psalm 107:1"},
    {"id": 58, "verse": "But the Lord stood at my side and gave me strength, so that through me the message might be fully proclaimed and all the Gentiles might hear it. And I was delivered from the lion’s mouth.", "book": "2 Timothy 4:17"},
    {"id": 59, "verse": "Your word is a lamp to my feet and a light to my path.", "book": "Psalm 119:105"},
    {"id": 60, "verse": "Be completely humble and gentle; be patient, bearing with one another in love.", "book": "Ephesians 4:2"},
    {"id": 61, "verse": "For the Spirit God gave us does not make us timid, but gives us power, love and self-discipline.", "book": "2 Timothy 1:7"},
    {"id": 62, "verse": "Surely your goodness and love will follow me all the days of my life, and I will dwell in the house of the Lord forever.", "book": "Psalm 23:6"},
    {"id": 63, "verse": "Finally, be strong in the Lord and in his mighty power.", "book": "Ephesians 6:10"},
    {"id": 64, "verse": "This is the day that the Lord has made; let us rejoice and be glad in it.", "book": "Psalm 118:24"},
    {"id": 65, "verse": "For where your treasure is, there your heart will be also.", "book": "Matthew 6:21"},
    {"id": 66, "verse": "The Lord your God is with you, the Mighty Warrior who saves. He will take great delight in you; in his love he will no longer rebuke you, but will rejoice over you with singing.", "book": "Zephaniah 3:17"},
    {"id": 67, "verse": "The name of the Lord is a fortified tower; the righteous run to it and are safe.", "book": "Proverbs 18:10"},
    {"id": 68, "verse": "I have told you these things, so that in me you may have peace. In this world you will have trouble. But take heart! I have overcome the world.", "book": "John 16:33"},
    {"id": 69, "verse": "Come to me, all you who are weary and burdened, and I will give you rest.", "book": "Matthew 11:28"},
    {"id": 70, "verse": "Therefore, there is now no condemnation for those who are in Christ Jesus.", "book": "Romans 8:1"},
    {"id": 71, "verse": "And we know that in all things God works for the good of those who love him, who have been called according to his purpose.", "book": "Romans 8:28"},
    {"id": 72, "verse": "Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God.", "book": "Philippians 4:6"},
    {"id": 73, "verse": "The Lord is my shepherd, I lack nothing.", "book": "Psalm 23:1"},
    {"id": 74, "verse": "Trust in the Lord with all your heart and lean not on your own understanding; in all your ways submit to him, and he will make your paths straight.", "book": "Proverbs 3:5-6"},
    {"id": 75, "verse": "But seek first his kingdom and his righteousness, and all these things will be given to you as well.", "book": "Matthew 6:33"},
    {"id": 76, "verse": "And my God will meet all your needs according to the riches of his glory in Christ Jesus.", "book": "Philippians 4:19"},
    {"id": 77, "verse": "He gives strength to the weary and increases the power of the weak.", "book": "Isaiah 40:29"},
    {"id": 78, "verse": "The Lord is good, a refuge in times of trouble. He cares for those who trust in him.", "book": "Nahum 1:7"},
    {"id": 79, "verse": "You will seek me and find me when you seek me with all your heart.", "book": "Jeremiah 29:13"},
    {"id": 80, "verse": "The Lord is my light and my salvation—whom shall I fear? The Lord is the stronghold of my life—of whom shall I be afraid?", "book": "Psalm 27:1"},
    {"id": 81, "verse": "The Lord makes firm the steps of the one who delights in him; though he may stumble, he will not fall, for the Lord upholds him with his hand.", "book": "Psalm 37:23-24"},
    {"id": 82, "verse": "He has shown you, O mortal, what is good. And what does the Lord require of you? To act justly and to love mercy and to walk humbly with your God.", "book": "Micah 6:8"},
    {"id": 83, "verse": "I keep my eyes always on the Lord. With him at my right hand, I will not be shaken.", "book": "Psalm 16:8"},
    {"id": 84, "verse": "Do not worry about tomorrow, for tomorrow will worry about itself. Each day has enough trouble of its own.", "book": "Matthew 6:34"},
    {"id": 85, "verse": "In the beginning was the Word, and the Word was with God, and the Word was God.", "book": "John 1:1"},
    {"id": 86, "verse": "And the peace of God, which transcends all understanding, will guard your hearts and your minds in Christ Jesus.", "book": "Philippians 4:7"},
    {"id": 87, "verse": "The Word became flesh and made his dwelling among us. We have seen his glory, the glory of the one and only Son, who came from the Father, full of grace and truth.", "book": "John 1:14"},
    {"id": 88, "verse": "But he was pierced for our transgressions, he was crushed for our iniquities; the punishment that brought us peace was on him, and by his wounds we are healed.", "book": "Isaiah 53:5"},
    {"id": 89, "verse": "The Lord your God is with you, the Mighty Warrior who saves. He will take great delight in you; in his love he will no longer rebuke you, but will rejoice over you with singing.", "book": "Zephaniah 3:17"},
    {"id": 90, "verse": "My flesh and my heart may fail, but God is the strength of my heart and my portion forever.", "book": "Psalm 73:26"},
    {"id": 91, "verse": "Be still, and know that I am God; I will be exalted among the nations, I will be exalted in the earth.", "book": "Psalm 46:10"},
    {"id": 92, "verse": "The Lord bless you and keep you; the Lord make his face shine on you and be gracious to you; the Lord turn his face toward you and give you peace.", "book": "Numbers 6:24-26"},
    {"id": 93, "verse": "But those who hope in the Lord will renew their strength. They will soar on wings like eagles; they will run and not grow weary, they will walk and not be faint.", "book": "Isaiah 40:31"},
    {"id": 94, "verse": "The Lord is close to the brokenhearted and saves those who are crushed in spirit.", "book": "Psalm 34:18"},
    {"id": 95, "verse": "Taste and see that the Lord is good; blessed is the one who takes refuge in him.", "book": "Psalm 34:8"},
    {"id": 96, "verse": "No weapon formed against you shall prosper, and every tongue which rises against you in judgment You shall condemn. This is the heritage of the servants of the Lord, and their righteousness is from Me, says the Lord.", "book": "Isaiah 54:17"},
    {"id": 97, "verse": "The Lord gives strength to his people; the Lord blesses his people with peace.", "book": "Psalm 29:11"},
    {"id": 98, "verse": "For we are God’s handiwork, created in Christ Jesus to do good works, which God prepared in advance for us to do.", "book": "Ephesians 2:10"},
    {"id": 99, "verse": "Jesus looked at them and said, 'With man this is impossible, but with God all things are possible.'", "book": "Matthew 19:26"},
    {"id": 100, "verse": "The Lord is my rock, my fortress and my deliverer; my God is my rock, in whom I take refuge, my shield and the horn of my salvation, my stronghold.", "book": "Psalm 18:2"}
]

# Route to get all Bible verses
@app.route('/verses', methods=['GET'])
def get_all_verses():
    # Return all verses as a JSON response
    return jsonify(bible_verses)

# Route to get a specific Bible verse by its ID
@app.route('/verse/<int:verse_id>', methods=['GET'])
def get_verse_by_id(verse_id):
    # Find the verse with the matching ID
    verse = next((verse for verse in bible_verses if verse['id'] == verse_id), None)
    
    # If the verse is not found, return an error message with a 404 status code
    if verse is None:
        return jsonify({"error": "Verse not found"}), 404
    
    # If the verse is found, return it as a JSON response
    return jsonify(verse)

# Start the Flask application on the specified port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
