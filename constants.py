PREFIX = "$"
HELP_MSG = "```COMMANDS :\n$balance\n$withdraw\n$deposit\n$work\n$rob\n$crime\n$beg\n$shop```"
OUTCOMES_WORK = {
    "You found a hidden treasure chest at work and earned $#": (50.0, 100.0),
    "Your boss gave you a surprise bonus of $# for your hard work": (100.0, 150.0),
    "You discovered a new way to save the company money and got a reward of $#": (75.0, 125.0),
    "You won the office lottery and received $#": (200.0, 300.0),
    "You fixed the coffee machine and everyone chipped in to give you $#": (20.0, 50.0),
    "You found a winning scratch-off ticket in the break room and won $#": (30.0, 60.0),
    "You helped a colleague with a project and they gave you $# as a thank you": (40.0, 80.0),
    "You found some extra cash in the vending machine and kept it, earning $#": (10.0, 25.0),
    "You completed a big project ahead of schedule and received a bonus of $#": (150.0, 250.0),
    "You found a forgotten envelope with $# in your desk drawer": (20.0, 40.0),
    "You organized the office party and got a tip of $#": (10.0, 30.0),
    "You won the 'Employee of the Month' award and received $#": (50.0, 100.0),
    "You found a valuable item at work and sold it for $#": (60.0, 120.0),
    "You helped fix a major issue and got a reward of $#": (80.0, 150.0),
    "You found a stash of petty cash and took $#": (5.0, 15.0)
}
OUTCOMES_CRIME = {
    "You successfully hacked into a bank and stole $#": (50.0, 100.0),
    "You pulled off a heist and got away with $#": (100.0, 150.0),
    "You pickpocketed a wealthy businessman and got $#": (30.0, 70.0),
    "You sold some 'hot' merchandise and earned $#": (80.0, 130.0),
    "You ran a successful scam and made $#": (60.0, 110.0),
    "You robbed a convenience store and got away with $#": (40.0, 90.0),
    "You mugged a tourist and found $# in their wallet": (20.0, 50.0),
    "You broke into a car and found $# in the glove compartment": (15.0, 35.0),
    "You stole a bike and sold it for $#": (25.0, 60.0),
    "You ran a counterfeit money operation and made $#": (70.0, 120.0),
    "You robbed a jewelry store and got away with $#": (200.0, 300.0),
    "You hijacked a truck and sold the goods for $#": (150.0, 250.0),
    "You ran an illegal gambling ring and earned $#": (100.0, 200.0),
    "You stole a purse and found $# inside": (10.0, 40.0),
    "You broke into a warehouse and found $# worth of goods": (80.0, 150.0)
}
OUTCOMES_BEG = {
    "A kind stranger felt sorry for you and gave you $#": (10.0, 25.0),
    "You found $# in an old coat pocket while begging": (25.0, 50.0),
    "A generous passerby handed you $#": (15.0, 30.0),
    "You sang a song and someone gave you $# for your effort": (5.0, 20.0),
    "You found a wallet with $# inside": (40.0, 60.0),
    "A child gave you their allowance of $#": (2.0, 10.0),
    "You found some loose change on the ground worth $#": (1.0, 5.0),
    "A street performer shared their earnings with you, giving you $#": (10.0, 20.0),
    "A tourist felt generous and gave you $#": (20.0, 40.0),
    "You found a $1 bill on the sidewalk": (1.0, 1.0),
    "A dog walker gave you some spare change worth $#": (3.0, 7.0),
    "You found a hidden stash of coins worth $#": (5.0, 15.0),
    "A busker gave you a portion of their earnings, totaling $#": (8.0, 18.0),
    "You found a $5 bill stuck in a bush": (5.0, 5.0),
    "A kind soul bought you a meal and gave you $#": (10.0, 25.0)
}