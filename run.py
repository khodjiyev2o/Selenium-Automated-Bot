from project.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.search(
        where = 'New York',
        check_in_date = '2022-06-27',
        check_out_date = '2022-06-28',
        guest_count = 3
    )
    bot.apply_filtrations()
    bot.refresh()
    bot.report_results()



