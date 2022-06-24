from project.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.search(
        where = input("Where are you going?\n"),
        check_in_date = input("Enter check-in date.For example:2022-06-25\n"),
        check_out_date = input("Enter check-out date.For example:2022-06-25\n"),
        guest_count = int(input("How many adults in total? \n"))
    )
    bot.apply_filtrations()
    bot.refresh()
    bot.show_results()



