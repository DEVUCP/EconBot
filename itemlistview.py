# In market_view.py
import discord
import utils
import singletons

class InventoryView(discord.ui.View):
    def __init__(self, original_user, item_list, market = False, timeout=180):
        super().__init__(timeout=timeout)
        self.original_user = original_user
        self.item_list = item_list
        self.market = market
        self.current_page = 0

    def IsOriginalUser(self, user : discord.User) -> bool:
        """Returns True if user is the same as the original user."""
        return user.id == self.original_user.id
    
    @discord.ui.button(label="<<", style=discord.ButtonStyle.grey)
    async def FirstButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Checks if the original user.
        if not self.IsOriginalUser(user=interaction.user):
            return

        self.current_page = 0
        await self.UpdateList(interaction)

    @discord.ui.button(label="<", style=discord.ButtonStyle.grey)
    async def PreviousButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Checks if the original user.
        if not self.IsOriginalUser(user=interaction.user):
            return

        self.current_page = max(0, self.current_page - 1) # Picks 0 minimum if current_page is negative (invalid index).
        await self.UpdateList(interaction)

    @discord.ui.button(label=">", style=discord.ButtonStyle.grey)
    async def NextButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Checks if the original user.
        if not self.IsOriginalUser(user=interaction.user):
            return
        
        self.current_page += 1 # Increment page.

         # If this index exists, then next page is valid.
        try :
            self.item_list[self.current_page]

        # if not then stay on last page.
        except IndexError: 
            self.current_page -= 1
        
        await self.UpdateList(interaction)

    @discord.ui.button(label=">>", style=discord.ButtonStyle.grey)
    async def Lastbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Checks if the original user.
        if not self.IsOriginalUser(user=interaction.user):
            return
        
        self.current_page = len(self.item_list) - 1
        await self.UpdateList(interaction)


    async def UpdateList(self, interaction) -> None:
        """Update the list embed based on the current page"""
        new_embed = CreateListEmbed(page=self.current_page, item_list=self.item_list, market=self.market)
        await interaction.response.edit_message(embed=new_embed)

    

class MarketView(discord.ui.View):
    def __init__(self, original_user, item_list, market = False, timeout=180):
        super().__init__(timeout=timeout)
        self.original_user = original_user
        self.item_list = item_list
        self.market = market
        self.current_page = 0

    def IsOriginalUser(self, user : discord.User) -> bool:
        """Returns True if user is the same as the original user."""
        return user.id == self.original_user.id

    @discord.ui.select(placeholder="Market", options=[
        discord.SelectOption(label="Market"),
        discord.SelectOption(label="Black Market")
    ])
    async def select_callback(self, interaction : discord.Interaction, select : discord.ui.Select):
        # Checks if the original user.
        if not self.IsOriginalUser(user=interaction.user):
            return
        
        if select.values[0] == "Market":
            market = CreateListEmbed(page=0, item_list=singletons.market_pages, market="Market")
            view = MarketView(interaction.user, item_list=singletons.market_pages, market="Market") # Creates New ItemListView

            await interaction.response.edit_message(embed=market, view=view)

        elif select.values[0] == "Black Market":
            blackmarket = CreateListEmbed(page=0, item_list=singletons.black_market_pages, market="Black Market")
            view = MarketView(interaction.user, item_list=singletons.black_market_pages, market="Black Market") # Creates New ItemListView

            await interaction.response.edit_message(embed=blackmarket, view=view)

    @discord.ui.button(label="<<", style=discord.ButtonStyle.grey)
    async def FirstButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Checks if the original user.
        if not self.IsOriginalUser(user=interaction.user):
            return

        self.current_page = 0
        await self.UpdateList(interaction)

    @discord.ui.button(label="<", style=discord.ButtonStyle.grey)
    async def PreviousButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Checks if the original user.
        if not self.IsOriginalUser(user=interaction.user):
            return

        self.current_page = max(0, self.current_page - 1) # Picks 0 minimum if current_page is negative (invalid index).
        await self.UpdateList(interaction)

    @discord.ui.button(label=">", style=discord.ButtonStyle.grey)
    async def NextButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Checks if the original user.
        if not self.IsOriginalUser(user=interaction.user):
            return
        
        self.current_page += 1 # Increment page.

         # If this index exists, then next page is valid.
        try :
            self.item_list[self.current_page]

        # if not then stay on last page.
        except IndexError: 
            self.current_page -= 1
        
        await self.UpdateList(interaction)

    @discord.ui.button(label=">>", style=discord.ButtonStyle.grey)
    async def Lastbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Checks if the original user.
        if not self.IsOriginalUser(user=interaction.user):
            return
        
        self.current_page = len(self.item_list) - 1
        await self.UpdateList(interaction)


    async def UpdateList(self, interaction) -> None:
        """Update the list embed based on the current page"""
        new_embed = CreateListEmbed(page=self.current_page, item_list=self.item_list, market=self.market)
        await interaction.response.edit_message(embed=new_embed)


def CreateListEmbed(page : int, item_list, market : str = "Inventory") -> discord.Embed:
    embed = discord.Embed(title=market,description="You can buy stuff here." if market != "Inventory" else "All your items.",color=0xffff00) # Create list Embed.
    embed = utils.GetEmbedItemList(item_list=item_list[page], embed=embed, market=True if market!="Inventory" else False) # Iterates through to retrieve and use items in list.
    embed.set_footer(text=f"Page {page}" if page >= 0 else f"Page {len(item_list) - 1}")
    return embed
    # Create and return the list embed for the given page
    # Use the existing logic from GetEmbedItemList, but paginate the items