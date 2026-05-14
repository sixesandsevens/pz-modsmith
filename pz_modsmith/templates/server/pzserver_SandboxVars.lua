SandboxVars = {
    VERSION = 6,
    -- Changing this also sets the "Population Multiplier" in Advanced Zombie Options. Default = Normal
    -- 1 = Insane
    -- 2 = Very High
    -- 3 = High
    -- 4 = Normal
    -- 5 = Low
    -- 6 = None
    Zombies = 4,
    -- How zombies are distributed across the map. Default = Urban Focused
    -- 1 = Urban Focused
    -- 2 = Uniform
    Distribution = 1,
    -- Controls whether some randomization is applied to zombie distribution.
    ZombieVoronoiNoise = true,
    -- How frequently new zombies are added to the world. Default = None
    -- 1 = High
    -- 2 = Normal
    -- 3 = Low
    -- 4 = None
    ZombieRespawn = 4,
    -- Zombie allowed to migrate to empty cells.
    ZombieMigrate = true,
    -- Default = 1 Hour, 30 Minutes
    -- 1 = 15 Minutes
    -- 2 = 30 Minutes
    -- 3 = 1 Hour
    -- 4 = 1 Hour, 30 Minutes
    -- 5 = 2 Hours
    -- 6 = 3 Hours
    -- 7 = 4 Hours
    -- 8 = 5 Hours
    -- 9 = 6 Hours
    -- 10 = 7 Hours
    -- 11 = 8 Hours
    -- 12 = 9 Hours
    -- 13 = 10 Hours
    -- 14 = 11 Hours
    -- 15 = 12 Hours
    -- 16 = 13 Hours
    -- 17 = 14 Hours
    -- 18 = 15 Hours
    -- 19 = 16 Hours
    -- 20 = 17 Hours
    -- 21 = 18 Hours
    -- 22 = 19 Hours
    -- 23 = 20 Hours
    -- 24 = 21 Hours
    -- 25 = 22 Hours
    -- 26 = 23 Hours
    -- 27 = Real-time
    DayLength = 4,
    StartYear = 1,
    -- Month in which the game starts. Default = July
    -- 1 = January
    -- 2 = February
    -- 3 = March
    -- 4 = April
    -- 5 = May
    -- 6 = June
    -- 7 = July
    -- 8 = August
    -- 9 = September
    -- 10 = October
    -- 11 = November
    -- 12 = December
    StartMonth = 7,
    -- Day of the month in which the games starts.
    StartDay = 9,
    -- Hour of the day in which the game starts. Default = 9 AM
    -- 1 = 7 AM
    -- 2 = 9 AM
    -- 3 = 12 PM
    -- 4 = 2 PM
    -- 5 = 5 PM
    -- 6 = 9 PM
    -- 7 = 12 AM
    -- 8 = 2 AM
    -- 9 = 5 AM
    StartTime = 2,
    -- Whether the time of day changes naturally, or it's always day/night. Default = Normal
    -- 1 = Normal
    -- 2 = Endless Day
    -- 3 = Endless Night
    DayNightCycle = 1,
    -- Whether weather changes or remains at a single state. Default = Normal
    -- 1 = Normal
    -- 2 = No Weather
    -- 3 = Endless Rain
    -- 4 = Endless Storm
    -- 5 = Endless Snow
    -- 6 = Endless Blizzard
    ClimateCycle = 1,
    -- Whether fog occurs naturally, never occurs, or is always present. Default = Normal
    -- 1 = Normal
    -- 2 = No Fog
    -- 3 = Endless Fog
    FogCycle = 1,
    -- How long after the default start date (July 9, 1993) that plumbing fixtures (eg. sinks) stop being infinite sources of water. Default = 0 - 30 Days
    -- 1 = Instant
    -- 2 = 0 - 30 Days
    -- 3 = 0 - 2 Months
    -- 4 = 0 - 6 Months
    -- 5 = 0 - 1 Year
    -- 6 = 0 - 5 Years
    -- 7 = 2 - 6 Months
    -- 8 = 6 - 12 Months
    -- 9 = Disabled
    WaterShut = 2,
    -- How long after the default start date (July 9, 1993) that the world's electricity turns off for good. Default = 14 - 30 Days
    -- 1 = Instant
    -- 2 = 14 - 30 Days
    -- 3 = 14 Days - 2 Months
    -- 4 = 14 Days - 6 Months
    -- 5 = 14 Days - 1 Year
    -- 6 = 14 Days - 5 Years
    -- 7 = 2 - 6 Months
    -- 8 = 6 - 12 Months
    -- 9 = Disabled
    ElecShut = 2,
    -- How long alarm batteries can last for after the power shuts off. Default = 0 - 30 Days
    -- 1 = Instant
    -- 2 = 0 - 30 Days
    -- 3 = 0 - 2 Months
    -- 4 = 0 - 6 Months
    -- 5 = 0 - 1 Year
    -- 6 = 0 - 5 Years
    AlarmDecay = 2,
    -- How long after the default start date (July 9, 1993) that plumbing fixtures (eg. sinks) stop being infinite sources of water. Min: -1 Max: 2147483647 Default: 14
    WaterShutModifier = 14,
    -- How long after the default start date (July 9, 1993) that the world's electricity turns off for good. Min: -1 Max: 2147483647 Default: 14
    ElecShutModifier = 14,
    -- How long alarm batteries can last for after the power shuts off. Min: -1 Max: 2147483647 Default: 14
    AlarmDecayModifier = 14,
    -- Any food that can rot or spoil. Min: 0.00 Max: 4.00 Default: 0.80
    FoodLootNew = 0.8,
    -- All other items that can be read, including books, fliers, and newspapers. Min: 0.00 Max: 4.00 Default: 0.60
    LiteratureLootNew = 0.6,
    -- Books that provide skill XP multipliers. Min: 0.00 Max: 4.00 Default: 0.60
    SkillBookLoot = 0.6,
    -- Items that teach recipes. Min: 0.00 Max: 4.00 Default: 0.60
    RecipeResourceLoot = 0.6,
    -- Medicine, bandages and first aid tools. Min: 0.00 Max: 4.00 Default: 0.60
    MedicalLootNew = 0.6,
    -- Fishing Rods, Tents, camping gear etc. Min: 0.00 Max: 4.00 Default: 0.60
    SurvivalGearsLootNew = 0.6,
    -- Canned and dried food, beverages. Min: 0.00 Max: 4.00 Default: 0.60
    CannedFoodLootNew = 0.6,
    -- Weapons that are not tools in other categories. Min: 0.00 Max: 4.00 Default: 0.60
    WeaponLootNew = 0.6,
    -- Also includes weapon attachments. Min: 0.00 Max: 4.00 Default: 1.20
    RangedWeaponLootNew = 1.2,
    -- Loose ammo, boxes and magazines. Min: 0.00 Max: 4.00 Default: 0.60
    AmmoLootNew = 0.6,
    -- Vehicle parts and the tools needed to install them. Min: 0.00 Max: 4.00 Default: 0.60
    MechanicsLootNew = 0.6,
    -- Everything else. Also affects foraging for all items in Town/Road zones. Min: 0.00 Max: 4.00 Default: 0.80
    OtherLootNew = 0.8,
    -- All wearable items that are not containers. Min: 0.00 Max: 4.00 Default: 0.60
    ClothingLootNew = 0.6,
    -- Backpacks and other wearable/equippable containers, eg. cases. Min: 0.00 Max: 4.00 Default: 0.60
    ContainerLootNew = 0.6,
    -- Keys for buildings/cars, key rings, and locks. Min: 0.00 Max: 4.00 Default: 0.40
    KeyLootNew = 0.4,
    -- VHS tapes and CDs. Min: 0.00 Max: 4.00 Default: 0.60
    MediaLootNew = 0.6,
    -- Spiffo items, plushies, and other collectible keepsake items eg. Photos. Min: 0.00 Max: 4.00 Default: 0.60
    MementoLootNew = 0.6,
    -- Items that are used in cooking, including those (eg. knives) which can be weapons. Does not include food. Includes both usable and unusable items. Min: 0.00 Max: 4.00 Default: 0.60
    CookwareLootNew = 0.6,
    -- Items and weapons that are used as ingredients for crafting or building. This is a general category that does not include items belonging to other categories such as Cookware or Medical. Does not include Tools. Min: 0.00 Max: 4.00 Default: 0.60
    MaterialLootNew = 0.6,
    -- Items and weapons which are used in both animal and plant agriculture, such as Seeds, Trowels, or Shovels. Min: 0.00 Max: 4.00 Default: 0.60
    FarmingLootNew = 0.6,
    -- Items and weapons which are Tools but don't fit in other categories such as Mechanics or Farming. Min: 0.00 Max: 4.00 Default: 0.60
    ToolLootNew = 0.6,
    -- <BHC> [!] It is recommended that you DO NOT change this. [!] <RGB:1,1,1>   Can be used to adjust the number of rolls made on loot tables when spawning loot. Will not reduce the number of rolls below 1. Can negatively affect performance if set to high values. It is highly recommended that this not be changed. Min: 0.10 Max: 100.00 Default: 1.00
    RollsMultiplier = 1.0,
    -- A comma-separated list of item types that won't spawn as ordinary loot.
    LootItemRemovalList = "",
    -- If enabled, items on the Loot Item Removal List, or that have their rarity set to 'None', will not spawn in randomised world stories.
    RemoveStoryLoot = false,
    -- If enabled, items on the Loot Item Removal List, or that have their rarity set to 'None', will not spawn worn by, or attached to, zombies.
    RemoveZombieLoot = false,
    -- If greater than 0, the spawn of loot is increased relative to the number of nearby zombies,  with the effect multiplied by this number. Min: 0 Max: 20 Default: 0
    ZombiePopLootEffect = 0,
    -- Min: 0.00 Max: 0.20 Default: 0.05
    InsaneLootFactor = 0.05,
    -- Min: 0.05 Max: 0.60 Default: 0.20
    ExtremeLootFactor = 0.2,
    -- Min: 0.20 Max: 1.00 Default: 0.60
    RareLootFactor = 0.6,
    -- Min: 0.60 Max: 2.00 Default: 1.00
    NormalLootFactor = 1.0,
    -- Min: 1.00 Max: 3.00 Default: 2.00
    CommonLootFactor = 2.0,
    -- Min: 2.00 Max: 4.00 Default: 3.00
    AbundantLootFactor = 3.0,
    -- The global temperature. Default = Normal
    -- 1 = Very Cold
    -- 2 = Cold
    -- 3 = Normal
    -- 4 = Hot
    -- 5 = Very Hot
    Temperature = 3,
    -- How often it rains. Default = Normal
    -- 1 = Very Dry
    -- 2 = Dry
    -- 3 = Normal
    -- 4 = Rainy
    -- 5 = Very Rainy
    Rain = 3,
    -- Number of days until the erosion system (which adds vines, long grass, new trees etc. to the world) will reach 100%% growth. Default = Slow (200 Days)
    -- 1 = Very Fast (20 Days)
    -- 2 = Fast (50 Days)
    -- 3 = Normal (100 Days)
    -- 4 = Slow (200 Days)
    -- 5 = Very Slow (500 Days)
    ErosionSpeed = 4,
    -- For a custom Erosion Speed. Zero means use the Erosion Speed option. Maximum is 36,500 days (approximately 100 years). Min: -1 Max: 36500 Default: 0
    ErosionDays = 0,
    -- The speed of plant growth. Default = Normal
    -- 1 = Very Fast
    -- 2 = Fast
    -- 3 = Normal
    -- 4 = Slow
    -- 5 = Very Slow
    Farming = 3,
    -- How long it takes for food to break down in a composter. Default = 2 Weeks
    -- 1 = 1 Week
    -- 2 = 2 Weeks
    -- 3 = 3 Weeks
    -- 4 = 4 Weeks
    -- 5 = 6 Weeks
    -- 6 = 8 Weeks
    -- 7 = 10 Weeks
    -- 8 = 12 Weeks
    CompostTime = 2,
    -- How fast the player's hunger, thirst, and fatigue will decrease. Default = Normal
    -- 1 = Very Fast
    -- 2 = Fast
    -- 3 = Normal
    -- 4 = Slow
    -- 5 = Very Slow
    StatsDecrease = 3,
    -- The abundance of items found in Foraging mode. Default = Normal
    -- 1 = Very Poor
    -- 2 = Poor
    -- 3 = Normal
    -- 4 = Abundant
    -- 5 = Very Abundant
    NatureAbundance = 3,
    -- How likely the player is to activate a house alarm when breaking into a new house. Default = Sometimes
    -- 1 = Never
    -- 2 = Extremely Rare
    -- 3 = Rare
    -- 4 = Sometimes
    -- 5 = Often
    -- 6 = Very Often
    Alarm = 4,
    -- How frequently the doors of homes and buildings will be locked when discovered. Default = Very Often
    -- 1 = Never
    -- 2 = Extremely Rare
    -- 3 = Rare
    -- 4 = Sometimes
    -- 5 = Often
    -- 6 = Very Often
    LockedHouses = 6,
    -- Spawn with Chips, a Water Bottle, a Small Backpack, a Baseball Bat, and a Hammer.
    StarterKit = false,
    -- Nutritional value of food affects the player's condition. Turning this off will stop the player gaining or losing weight.
    Nutrition = true,
    -- How fast that food will spoil, inside or outside of a fridge. Default = Normal
    -- 1 = Very Fast
    -- 2 = Fast
    -- 3 = Normal
    -- 4 = Slow
    -- 5 = Very Slow
    FoodRotSpeed = 3,
    -- How effective a fridge will be at keeping food fresh for longer. Default = Normal
    -- 1 = Very Low
    -- 2 = Low
    -- 3 = Normal
    -- 4 = High
    -- 5 = Very High
    -- 6 = No decay
    FridgeFactor = 3,
    -- When greater than 0, loot will not respawn in zones that have been visited within this number of in-game hours. Min: 0 Max: 2147483647 Default: 0
    SeenHoursPreventLootRespawn = 0,
    -- When greater than 0, after X hours, all containers in towns and trailer parks in the world will respawn loot. To spawn loot a container must have been looted at least once. Loot respawn is not impacted by visibility or subsequent looting. Min: 0 Max: 2147483647 Default: 0
    HoursForLootRespawn = 0,
    -- Containers with a number of items greater, or equal to, this setting will not respawn. Min: 0 Max: 2147483647 Default: 5
    MaxItemsForLootRespawn = 5,
    -- Items will not respawn in buildings that players have barricaded or built in.
    ConstructionPreventsLootRespawn = true,
    -- A comma-separated list of item types that will be removed after HoursForWorldItemRemoval hours.
    WorldItemRemovalList = "Base.Hat, Base.Glasses, Base.Maggots, Base.Slug, Base.Slug2, Base.Snail, Base.Worm, Base.Dung_Mouse, Base.Dung_Rat",
    -- Number of hours since an item was dropped on the ground before it is removed.  Items are removed the next time that part of the map is loaded.   Zero means items are not removed. Min: 0.00 Max: 2147483647.00 Default: 24.00
    HoursForWorldItemRemoval = 24.0,
    -- If true, any items *not* in WorldItemRemovalList will be removed.
    ItemRemovalListBlacklistToggle = false,
    -- How long after the end of the world to begin. This will affect starting world erosion and food spoilage. Does not affect the starting date. Default = 0
    -- 1 = 0
    -- 2 = 1
    -- 3 = 2
    -- 4 = 3
    -- 5 = 4
    -- 6 = 5
    -- 7 = 6
    -- 8 = 7
    -- 9 = 8
    -- 10 = 9
    -- 11 = 10
    -- 12 = 11
    -- 13 = 12
    TimeSinceApo = 1,
    -- How much water plants will lose per day, and their ability to avoid disease. Default = Normal
    -- 1 = Very High
    -- 2 = High
    -- 3 = Normal
    -- 4 = Low
    -- 5 = Very Low
    PlantResilience = 3,
    -- The yield of plants when harvested. Default = Normal
    -- 1 = Very Poor
    -- 2 = Poor
    -- 3 = Normal
    -- 4 = Abundant
    -- 5 = Very Abundant
    PlantAbundance = 3,
    -- Recovery from being tired after performing actions. Default = Normal
    -- 1 = Very Fast
    -- 2 = Fast
    -- 3 = Normal
    -- 4 = Slow
    -- 5 = Very Slow
    EndRegen = 3,
    -- How regularly a helicopter passes over the Event Zone. Default = Once
    -- 1 = Never
    -- 2 = Once
    -- 3 = Sometimes
    -- 4 = Often
    Helicopter = 2,
    -- How often zombie-attracting metagame events like distant gunshots will occur. Default = Sometimes
    -- 1 = Never
    -- 2 = Sometimes
    -- 3 = Often
    MetaEvent = 2,
    -- How often events during the player's sleep, like nightmares, occur. Default = Never
    -- 1 = Never
    -- 2 = Sometimes
    -- 3 = Often
    SleepingEvent = 1,
    -- How much fuel is consumed by generators per in-game hour. Min: 0.00 Max: 100.00 Default: 0.10
    GeneratorFuelConsumption = 0.1,
    -- The chance of electrical generators spawning on the map. Default = Rare
    -- 1 = None (not recommended)
    -- 2 = Insanely Rare
    -- 3 = Extremely Rare
    -- 4 = Rare
    -- 5 = Normal
    -- 6 = Common
    -- 7 = Abundant
    GeneratorSpawning = 4,
    -- How often a looted map will have notes on it, written by a deceased survivor. Default = Sometimes
    -- 1 = Never
    -- 2 = Extremely Rare
    -- 3 = Rare
    -- 4 = Sometimes
    -- 5 = Often
    -- 6 = Very Often
    AnnotatedMapChance = 4,
    -- Adds free points during character creation. Min: -100 Max: 100 Default: 0
    CharacterFreePoints = 0,
    -- Gives player-built constructions extra hit points so they are  more resistant to zombie damage. Default = Normal
    -- 1 = Very Low
    -- 2 = Low
    -- 3 = Normal
    -- 4 = High
    -- 5 = Very High
    ConstructionBonusPoints = 3,
    -- The level of ambient lighting at night. Default = Normal
    -- 1 = Pitch Black
    -- 2 = Dark
    -- 3 = Normal
    -- 4 = Bright
    NightDarkness = 3,
    -- The time from dusk to dawn. Default = Normal
    -- 1 = Always Night
    -- 2 = Long
    -- 3 = Normal
    -- 4 = Short
    -- 5 = Always Day
    NightLength = 3,
    -- If survivors can get broken limbs from impacts, zombie damage, falls etc.
    BoneFracture = true,
    -- The impact that injuries have on your body, and their healing time. Default = Normal
    -- 1 = Low
    -- 2 = Normal
    -- 3 = High
    InjurySeverity = 2,
    -- How long, in hours, before dead zombie bodies disappear from the world.  If 0, maggots will not spawn on corpses. Min: -1.00 Max: 2147483647.00 Default: 216.00
    HoursForCorpseRemoval = 216.0,
    -- The impact that nearby decaying bodies has on the player's health and emotions. Default = Normal
    -- 1 = None
    -- 2 = Low
    -- 3 = Normal
    -- 4 = High
    -- 5 = Insane
    DecayingCorpseHealthImpact = 3,
    -- Whether nearby "living" zombies have the same impact on the player's health and emotions.
    ZombieHealthImpact = false,
    -- How much blood is sprayed on floors and walls by injuries. Default = Normal
    -- 1 = None
    -- 2 = Low
    -- 3 = Normal
    -- 4 = High
    -- 5 = Ultra Gore
    BloodLevel = 3,
    -- How quickly clothing degrades, becomes dirty, and bloodied. Default = Normal
    -- 1 = Disabled
    -- 2 = Slow
    -- 3 = Normal
    -- 4 = Fast
    ClothingDegradation = 3,
    -- If fires spread when started.
    FireSpread = true,
    -- Number of in-game days before rotten food is removed from the map.  -1 means rotten food is never removed. Min: -1 Max: 2147483647 Default: -1
    DaysForRottenFoodRemoval = -1,
    -- If enabled, generators will work on exterior tiles.  This will allow, for example, the powering of gas pumps.
    AllowExteriorGenerator = true,
    -- Maximum intensity of fog. Default = Normal
    -- 1 = Normal
    -- 2 = Moderate
    -- 3 = Low
    -- 4 = None
    MaxFogIntensity = 1,
    -- Maximum intensity of rain. Default = Normal
    -- 1 = Normal
    -- 2 = Moderate
    -- 3 = Low
    MaxRainFxIntensity = 1,
    -- If snow will accumulate on the ground.  If disabled, snow will still show on vegetation and rooftops.
    EnableSnowOnGround = true,
    -- If melee attacking slows you down.
    AttackBlockMovements = true,
    -- The chance of finding randomized buildings on the map (eg. burnt out houses,  ones containing loot stashes or dead bodies). Default = Rare
    -- 1 = Never
    -- 2 = Extremely Rare
    -- 3 = Rare
    -- 4 = Sometimes
    -- 5 = Often
    -- 6 = Very Often
    -- 7 = Always Tries
    SurvivorHouseChance = 3,
    -- The chance of road stories (eg. police roadblocks) spawning. Default = Rare
    -- 1 = Never
    -- 2 = Extremely Rare
    -- 3 = Rare
    -- 4 = Sometimes
    -- 5 = Often
    -- 6 = Very Often
    -- 7 = Always Tries
    VehicleStoryChance = 3,
    -- The chance of stories specific to map zones (eg. a campsite in a forest) spawning. Default = Rare
    -- 1 = Never
    -- 2 = Extremely Rare
    -- 3 = Rare
    -- 4 = Sometimes
    -- 5 = Often
    -- 6 = Very Often
    -- 7 = Always Tries
    ZoneStoryChance = 3,
    -- Allows you to select from every piece of clothing in the game when customizing your character
    AllClothesUnlocked = false,
    -- If tainted water will show a warning marking it as such.
    EnableTaintedWaterText = true,
    -- If vehicles will spawn.
    EnableVehicles = true,
    -- How frequently vehicles can be discovered on the map. Default = Low
    -- 1 = None
    -- 2 = Very Low
    -- 3 = Low
    -- 4 = Normal
    -- 5 = High
    CarSpawnRate = 3,
    -- General engine loudness to zombies. Min: 0.00 Max: 100.00 Default: 1.00
    ZombieAttractionMultiplier = 1.0,
    -- Whether found vehicles are locked, need keys to start etc.
    VehicleEasyUse = false,
    -- How full the gas tank of discovered vehicles will be. Default = Low
    -- 1 = Very Low
    -- 2 = Low
    -- 3 = Normal
    -- 4 = High
    -- 5 = Very High
    -- 6 = Full
    InitialGas = 2,
    -- If enabled, gas pumps will never run out of fuel
    FuelStationGasInfinite = false,
    -- The minimum amount of gasoline that can spawn in gas pumps. Check the "Advanced" box below to use a custom amount. Min: 0.00 Max: 1.00 Default: 0.00
    FuelStationGasMin = 0.0,
    -- The maximum amount of gasoline that can spawn in gas pumps. Check the "Advanced" box below to use a custom amount. Min: 0.00 Max: 1.00 Default: 0.80
    FuelStationGasMax = 0.8,
    -- The chance, as a percentage, that individual gas pumps will initially have no fuel. Min: 0 Max: 100 Default: 20
    FuelStationGasEmptyChance = 20,
    -- How likely cars will be locked Default = Sometimes
    -- 1 = Never
    -- 2 = Extremely Rare
    -- 3 = Rare
    -- 4 = Sometimes
    -- 5 = Often
    -- 6 = Very Often
    LockedCar = 4,
    -- How gas-hungry vehicles are. Min: 0.00 Max: 100.00 Default: 1.00
    CarGasConsumption = 1.0,
    -- General condition discovered vehicles will be in. Default = Normal
    -- 1 = Very Low
    -- 2 = Low
    -- 3 = Normal
    -- 4 = High
    -- 5 = Very High
    CarGeneralCondition = 3,
    -- The amount of damage dealt to vehicles that crash. Default = Normal
    -- 1 = Very Low
    -- 2 = Low
    -- 3 = Normal
    -- 4 = High
    -- 5 = Very High
    CarDamageOnImpact = 3,
    -- Damage received by the player from being crashed into. Default = None
    -- 1 = None
    -- 2 = Low
    -- 3 = Normal
    -- 4 = High
    -- 5 = Very High
    DamageToPlayerFromHitByACar = 1,
    -- If traffic jams consisting of wrecked cars  will appear on main roads.
    TrafficJam = true,
    -- How frequently discovered vehicles have active alarms. Default = Rare
    -- 1 = Never
    -- 2 = Extremely Rare
    -- 3 = Rare
    -- 4 = Sometimes
    -- 5 = Often
    -- 6 = Very Often
    CarAlarm = 3,
    -- If the player can get injured from being in a car accident.
    PlayerDamageFromCrash = true,
    -- How many in-game hours before a wailing siren shuts off. Min: 0.00 Max: 168.00 Default: 0.00
    SirenShutoffHours = 0.0,
    -- The chance of finding a vehicle with gas in its tank. Default = Normal
    -- 1 = Low
    -- 2 = Normal
    -- 3 = High
    ChanceHasGas = 2,
    -- Whether a player can discover a car that has been cared for  after the Knox infection struck. Default = Low
    -- 1 = None
    -- 2 = Low
    -- 3 = Normal
    -- 4 = High
    RecentlySurvivorVehicles = 2,
    -- If certain melee weapons will be able to strike multiple zombies in one hit.
    MultiHitZombies = false,
    -- Chance of being bitten when a zombie attacks from behind. Default = High
    -- 1 = Low
    -- 2 = Medium
    -- 3 = High
    RearVulnerability = 3,
    -- If zombies will head towards the sound of vehicle sirens.
    SirenEffectsZombies = true,
    -- Speed at which animals stats (hunger, thirst etc.) reduce. Default = Normal
    -- 1 = Ultra Fast
    -- 2 = Very Fast
    -- 3 = Fast
    -- 4 = Normal
    -- 5 = Slow
    -- 6 = Very Slow
    AnimalStatsModifier = 4,
    -- Speed at which animals stats (hunger, thirst etc.) reduce while in meta. Default = Normal
    -- 1 = Ultra Fast
    -- 2 = Very Fast
    -- 3 = Fast
    -- 4 = Normal
    -- 5 = Slow
    -- 6 = Very Slow
    AnimalMetaStatsModifier = 4,
    -- How long animals will be pregnant for before giving birth. Default = Normal
    -- 1 = Ultra Fast
    -- 2 = Very Fast
    -- 3 = Fast
    -- 4 = Normal
    -- 5 = Slow
    -- 6 = Very Slow
    AnimalPregnancyTime = 4,
    -- Speed at which animals age. Default = Normal
    -- 1 = Ultra Fast
    -- 2 = Very Fast
    -- 3 = Fast
    -- 4 = Normal
    -- 5 = Slow
    -- 6 = Very Slow
    AnimalAgeModifier = 4,
    -- Default = Normal
    -- 1 = Ultra Fast
    -- 2 = Very Fast
    -- 3 = Fast
    -- 4 = Normal
    -- 5 = Slow
    -- 6 = Very Slow
    AnimalMilkIncModifier = 4,
    -- Default = Normal
    -- 1 = Ultra Fast
    -- 2 = Very Fast
    -- 3 = Fast
    -- 4 = Normal
    -- 5 = Slow
    -- 6 = Very Slow
    AnimalWoolIncModifier = 4,
    -- The chance of finding animals in farm. Default = Often
    -- 1 = Never
    -- 2 = Extremely Rare
    -- 3 = Rare
    -- 4 = Sometimes
    -- 5 = Often
    -- 6 = Very Often
    -- 7 = Always
    AnimalRanchChance = 5,
    -- The number of hours grass will regrow after being  eaten by an animal or cut by the player. Min: 1 Max: 9999 Default: 240
    AnimalGrassRegrowTime = 240,
    -- If a meta (ie. not actually visible in-game) fox may attack  your chickens if the hutch's door is left open at night.
    AnimalMetaPredator = false,
    -- If animals with a mating season will respect it.  Otherwise they can reproduce/lay eggs all year round.
    AnimalMatingSeason = true,
    -- How long before baby animals will hatch from eggs. Default = Normal
    -- 1 = Ultra Fast
    -- 2 = Very Fast
    -- 3 = Fast
    -- 4 = Normal
    -- 5 = Slow
    -- 6 = Very Slow
    AnimalEggHatch = 4,
    -- If true, animal calls will attract nearby zombies.
    AnimalSoundAttractZombies = true,
    -- The chance of animals leaving tracks. Default = Sometimes
    -- 1 = Never
    -- 2 = Extremely Rare
    -- 3 = Rare
    -- 4 = Sometimes
    -- 5 = Often
    -- 6 = Very Often
    AnimalTrackChance = 4,
    -- The chance of creating a path for animals to be hunted. Default = Sometimes
    -- 1 = Never
    -- 2 = Extremely Rare
    -- 3 = Rare
    -- 4 = Sometimes
    -- 5 = Often
    -- 6 = Very Often
    AnimalPathChance = 4,
    -- The frequency and intensity of eg. rats in infested buildings. Min: 0 Max: 50 Default: 25
    MaximumRatIndex = 25,
    -- How long it takes for the Maximum Vermin Index to be reached. Min: 0 Max: 365 Default: 90
    DaysUntilMaximumRatIndex = 90,
    -- If a piece of media hasn't been fully seen or read, this setting determines whether it's displayed fully, displayed as "???", or hidden completely. Default = Completely hidden
    -- 1 = Fully revealed
    -- 2 = Shown as ???
    -- 3 = Completely hidden
    MetaKnowledge = 3,
    -- If true, you will be able to see any recipes that can be done with a station, even if you haven't learnt them yet.
    SeeNotLearntRecipe = true,
    -- If a building has more than this amount of rooms it will not be looted. Min: 0 Max: 200 Default: 50
    MaximumLootedBuildingRooms = 50,
    -- If poison can be added to food. Default = True
    -- 1 = True
    -- 2 = False
    -- 3 = Only bleach poisoning is disabled
    EnablePoisoning = 1,
    -- If/when maggots can spawn in corpses. Default = In and Around Bodies
    -- 1 = In and Around Bodies
    -- 2 = In Bodies Only
    -- 3 = Never
    MaggotSpawn = 1,
    -- The higher the value, the longer lightbulbs last before breaking.  If 0, lightbulbs will never break.  Does not affect vehicle headlights. Min: 0.00 Max: 1000.00 Default: 2.00
    LightBulbLifespan = 2.0,
    -- The abundance of fish in rivers and lakes. Default = Poor
    -- 1 = Very Poor
    -- 2 = Poor
    -- 3 = Normal
    -- 4 = Abundant
    -- 5 = Very Abundant
    FishAbundance = 2,
    -- When a skill is at this level or above, television/VHS/other media  will not provide XP for it. Min: 0 Max: 10 Default: 3
    LevelForMediaXPCutoff = 3,
    -- When a skill is at this level or above, scrapping furniture does not provide XP for the relevant skill. Does not apply to Electrical. Min: 0 Max: 10 Default: 0
    LevelForDismantleXPCutoff = 0,
    -- Number of days before old blood splats are removed. Removal happens when map chunks are loaded. 0 means they will never disappear. Min: 0 Max: 365 Default: 0
    BloodSplatLifespanDays = 0,
    -- Number of days before one can benefit from reading previously read literature items. Min: 1 Max: 365 Default: 45
    LiteratureCooldown = 45,
    -- If there are diminishing returns on bonus trait points provided from selecting multiple negative traits. Default = None
    -- 1 = None
    -- 2 = 1 point penalty for every 3 negative traits selected
    -- 3 = 1 point penalty for every 2 negative traits selected
    -- 4 = 1 point penalty for every negative trait selected after the first
    NegativeTraitsPenalty = 1,
    -- The number of in-game minutes it takes to read one page of a skill book. Min: 0.00 Max: 60.00 Default: 2.00
    MinutesPerPage = 2.0,
    -- When enabled, crops and herbs grown inside buildings will die. Does not affect houseplants.
    KillInsideCrops = true,
    -- When enabled, the growth of plants is affected by seasons.
    PlantGrowingSeasons = true,
    -- <BHC> [!] It is recommended that you DO NOT change this. Changing this can result in performance issues. [!] <RGB:1,1,1>   When enabled, dirt can be placed, and farming performed on other than the ground level.
    PlaceDirtAboveground = false,
    -- The speed of plant growth. Min: 0.10 Max: 100.00 Default: 1.00
    FarmingSpeedNew = 1.0,
    -- The abundance of harvested crops. Min: 0.10 Max: 10.00 Default: 1.00
    FarmingAmountNew = 1.0,
    -- The chance that any building will already be looted when found. Check the "Advanced" box below to use a custom number. Min: 0 Max: 200 Default: 25
    MaximumLooted = 25,
    -- How long it takes for Maximum Looted Building Chance to be reached. Min: 0 Max: 3650 Default: 90
    DaysUntilMaximumLooted = 90,
    -- The chance that any rural building will already be looted when found. Check the "Advanced" box below to use a custom number. Min: 0.00 Max: 2.00 Default: 0.50
    RuralLooted = 0.5,
    -- The maximum loot that won't spawn when Days Until Maximum Diminished Loot is reached. Check the "Advanced" box below to use an exact percentage. Min: 0 Max: 100 Default: 20
    MaximumDiminishedLoot = 20,
    -- How long it takes for Maximum Diminished Loot Percentage to be reached. Min: 0 Max: 3650 Default: 3650
    DaysUntilMaximumDiminishedLoot = 3650,
    -- Functions as a multiplier when applying muscle strain from swinging weapons or carrying heavy loads. Min: 0.00 Max: 10.00 Default: 0.70
    MuscleStrainFactor = 0.7,
    -- Functions as a multiplier when applying discomfort from worn items. Min: 0.00 Max: 10.00 Default: 0.80
    DiscomfortFactor = 0.8,
    -- If greater than zero damage can be taken from serious wound infections. Min: 0.00 Max: 10.00 Default: 1.00
    WoundInfectionFactor = 1.0,
    -- If true clothing with randomized tints will not be so dark to be virtually black.
    NoBlackClothes = true,
    -- Disables the failure chances when climbing sheet ropes or over walls.
    EasyClimbing = false,
    -- The maximum hours of fuel that can be placed in a campfire, wood stove etc. Min: 1 Max: 168 Default: 8
    MaximumFireFuelHours = 8,
    -- Replaces Chance-To-Hit mechanics with Chance-To-Damage calculations.  This mode prioritizes player aiming. Default = Zombies only
    -- 1 = Disabled
    -- 2 = Zombies only
    -- 3 = All types of target
    FirearmUseDamageChance = 2,
    -- A multiplier for the distance at which zombies can hear gunshots. Min: 0.20 Max: 2.00 Default: 1.00
    FirearmNoiseMultiplier = 1.0,
    -- Multiplier for firearm jamming chance. 0 disables jamming. Min: 0.00 Max: 10.00 Default: 1.00
    FirearmJamMultiplier = 1.0,
    -- Multiplier for Moodle effects on hit chance. 0 disables Moodle penalty. Min: 0.00 Max: 10.00 Default: 1.00
    FirearmMoodleMultiplier = 1.0,
    -- Multiplier for the effects of weather (wind, rain and fog) on hit chance. 0 disables weather effect. Min: 0.00 Max: 10.00 Default: 1.00
    FirearmWeatherMultiplier = 1.0,
    -- Enable to have headgear like welding masks affect hit chance
    FirearmHeadGearEffect = true,
    -- Chance to turn a dirt floor into a clay floor. Applies to lakes. Min: 0.00 Max: 1.00 Default: 0.05
    ClayLakeChance = 0.05,
    -- Chance to turn a dirt floor into a clay floor. Applies to rivers. Min: 0.00 Max: 1.00 Default: 0.05
    ClayRiverChance = 0.05,
    -- Min: 1 Max: 100 Default: 20
    GeneratorTileRange = 20,
    -- How many levels both above and below a generator it can provide with electricity. Min: 1 Max: 15 Default: 3
    GeneratorVerticalPowerRange = 3,
    -- Allows the Scamp Camper Trailer to spawn. Uncheck to disable camper spawns.
    FR_RVsOnly_UnblockCamperScamp = true,
    -- Allows F700 Propane Truck to spawn
    FR_RVsOnly_UnblockPropaneTruck = false,
    -- Allows F700 Fuel Truck to spawn
    FR_RVsOnly_UnblockFuelTruck = false,
    -- Allows Small and Medium Fuel Trailers to spawn
    FR_RVsOnly_UnblockFuelTrailers = false,
    -- Allows Ford F700 and Isuzu NRR Box Trucks to spawn.
    FR_RVsOnly_UnblockBoxTrucks = false,
    -- Allows Semi-Van and Container trailers to spawn.
    FR_RVsOnly_UnblockSemiTrailers = false,
    -- Allows the Peterbilt 359 (Short, Med, Long) to spawn, for pulling semi trailers
    FR_RVsOnly_UnblockPeterbilt = false,
    -- Allows Medium and Large moving trailers to spawn.
    FR_RVsOnly_UnblockCarTrailers = false,
    -- Allows the Dodge Ram Moving Van variant to spawn.
    FR_RVsOnly_UnblockRamMoving = false,
    -- Allows the GM New Look Transit Bus to spawn.
    FR_RVsOnly_UnblockGMNewLook = false,
    -- Allows the Ford B700 Prison Bus variant to spawn.
    FR_RVsOnly_UnblockPrisonBus = false,
    -- Allows Long and Short School Bus variants to spawn.
    FR_RVsOnly_UnblockSchoolBuses = false,
    -- Allows Chevrolet Stepvans (Standard and Police) to spawn.
    FR_RVsOnly_UnblockStepvans = false,
    -- Allows standard Ford Econoline and Florist variants to spawn.
    FR_RVsOnly_UnblockEconolineVans = false,
    -- Allows the 1992 Chevy Astro van to spawn.
    FR_RVsOnly_UnblockAstroVan = false,
    -- Allows the Grumman LLV postal vehicle to spawn.
    FR_RVsOnly_UnblockPostalVan = false,
    -- Allows the Ford Econoline Ambulance to spawn.
    FR_RVsOnly_UnblockEconolineAmbulance = false,
    -- Allows the Ford F350 Ambulance to spawn.
    FR_RVsOnly_UnblockF350Ambulance = false,
    -- Allows the Pierce Fire Engine to spawn.
    FR_RVsOnly_UnblockFireTruck = false,
    -- Parts with a success chance below this value will be skipped during training. <LINE> At '-1' this setting is not enforced, any value over '-1' is enforced server-wide. <LINE>  <LINE> 0%% -> All parts will be worked on. Parts will break at lower skill levels. <LINE> 30%% -> Default setting for a good balance. <LINE> 100%% -> Only parts that are guaranteed to succeed will be worked on. Completely safe at all skill levels. Min: -1 Max: 100 Default: -1
    BAM_Server_MinSuccessChance = -1,
    -- Drop Rate Multiplier Min: 0.00 Max: 9999.00 Default: 0.10
    AmmoLootDropCarton_Normal = 0.1,
    -- Drop Rate Multiplier Min: 0.00 Max: 9999.00 Default: 1.00
    AmmoLootDropBox_Normal = 1.0,
    -- Drop Rate Multiplier Min: 0.00 Max: 9999.00 Default: 20.00
    AmmoLootDrop_Normal = 20.0,
    Basement = {
        -- How frequently basements spawn at random locations. Default = Sometimes
        -- 1 = Never
        -- 2 = Extremely Rare
        -- 3 = Rare
        -- 4 = Sometimes
        -- 5 = Often
        -- 6 = Very Often
        -- 7 = Always
        SpawnFrequency = 4,
    },
    Map = {
        -- If enabled, a mini-map window will be available.
        AllowMiniMap = false,
        -- If enabled, the world map can be accessed.
        AllowWorldMap = true,
        -- If enabled, the world map will be completely filled in on starting the game.
        MapAllKnown = false,
        -- If enabled, maps can't be read unless there's a source of light available.
        MapNeedsLight = true,
    },
    ZombieLore = {
        -- How fast zombies move. Default = Random
        -- 1 = Sprinters
        -- 2 = Fast Shamblers
        -- 3 = Shamblers
        -- 4 = Random
        Speed = 4,
        -- If Random Speed is enabled, this controls what percentage of zombies are Sprinters. Check the "Advanced" box below to use a custom percentage. Min: 0 Max: 100 Default: 0
        SprinterPercentage = 0,
        -- The damage zombies inflict per attack. Default = Normal
        -- 1 = Superhuman
        -- 2 = Normal
        -- 3 = Weak
        -- 4 = Random
        Strength = 2,
        -- The difficulty of killing a zombie. Default = Random
        -- 1 = Tough
        -- 2 = Normal
        -- 3 = Fragile
        -- 4 = Random
        Toughness = 4,
        -- How the Knox Virus spreads. Default = Blood and Saliva
        -- 1 = Blood and Saliva
        -- 2 = Saliva Only
        -- 3 = Everyone's Infected
        -- 4 = None
        Transmission = 1,
        -- How quickly the infection takes effect. Default = 2-3 Days
        -- 1 = Instant
        -- 2 = 0-30 Seconds
        -- 3 = 0-1 Minutes
        -- 4 = 0-12 Hours
        -- 5 = 2-3 Days
        -- 6 = 1-2 Weeks
        -- 7 = Never
        Mortality = 5,
        -- How quickly infected corpses rise as zombies. Default = 0-1 Minutes
        -- 1 = Instant
        -- 2 = 0-30 Seconds
        -- 3 = 0-1 Minutes
        -- 4 = 0-12 Hours
        -- 5 = 2-3 Days
        -- 6 = 1-2 Weeks
        Reanimate = 3,
        -- Zombie intelligence. Default = Basic Navigation
        -- 1 = Navigate and Use Doors
        -- 2 = Navigate
        -- 3 = Basic Navigation
        -- 4 = Random
        Cognition = 3,
        -- Min: 0 Max: 100 Default: 0
        DoorOpeningPercentage = 0,
        -- How often zombies can crawl under parked vehicles. Default = Often
        -- 1 = Crawlers Only
        -- 2 = Extremely Rare
        -- 3 = Rare
        -- 4 = Sometimes
        -- 5 = Often
        -- 6 = Very Often
        -- 7 = Always
        CrawlUnderVehicle = 5,
        -- How long zombies remember a player after seeing or hearing them. Default = Normal
        -- 1 = Long
        -- 2 = Normal
        -- 3 = Short
        -- 4 = None
        -- 5 = Random
        -- 6 = Random between Normal and None
        Memory = 2,
        -- Zombie vision radius. Default = Random between Normal and Poor
        -- 1 = Eagle
        -- 2 = Normal
        -- 3 = Poor
        -- 4 = Random
        -- 5 = Random between Normal and Poor
        Sight = 5,
        -- Zombie hearing radius. Default = Random between Normal and Poor
        -- 1 = Pinpoint
        -- 2 = Normal
        -- 3 = Poor
        -- 4 = Random
        -- 5 = Random between Normal and Poor
        Hearing = 5,
        -- Activates the new advanced stealth mechanics, which allows you to hide from zombies behind cars, takes traits and weather into account, and much more.
        SpottedLogic = true,
        -- If zombies that have not seen/heard player can attack doors and constructions while roaming.
        ThumpNoChasing = false,
        -- If zombies can destroy player constructions and defenses.
        ThumpOnConstruction = true,
        -- Whether zombies are more "active" during the day or night.  "Active" zombies will use the speed set in the "Speed" setting.  "Inactive" zombies will be slower, and tend not to give chase. Default = Both
        -- 1 = Both
        -- 2 = Night
        -- 3 = Day
        ActiveOnly = 1,
        -- If zombies trigger house alarms when breaking through windows or doors.
        TriggerHouseAlarm = true,
        -- If multiple attacking zombies can drag you down and kill you.  Dependent on zombie strength.
        ZombiesDragDown = true,
        -- If crawler zombies beside a player contribute to the chance of being dragged down and killed by a group of zombies.
        ZombiesCrawlersDragDown = false,
        -- If zombies have a chance to lunge at you after climbing over a fence or through a window if you're too close.
        ZombiesFenceLunge = true,
        -- Serves as a multiplier when determining the effectiveness of armor worn by zombies. Min: 0.00 Max: 100.00 Default: 2.00
        ZombiesArmorFactor = 2.0,
        -- The maximum defense percentage that any worn protective garments can provide to a zombie. Min: 0 Max: 100 Default: 85
        ZombiesMaxDefense = 85,
        -- Percentage chance of having a random attached weapon. Min: 0 Max: 100 Default: 6
        ChanceOfAttachedWeapon = 6,
        -- How much damage zombies take when falling from height. Min: 0.00 Max: 100.00 Default: 1.00
        ZombiesFallDamage = 1.0,
        -- Whether some dead-looking zombies will reanimate and attack the player. Default = World Zombies
        -- 1 = World Zombies
        -- 2 = World and Combat Zombies
        -- 3 = Never
        DisableFakeDead = 1,
        -- Zombies will not spawn where players spawn. Default = Inside the building and around it
        -- 1 = Inside the building and around it
        -- 2 = Inside the building
        -- 3 = Inside the room
        -- 4 = Zombies can spawn anywhere
        PlayerSpawnZombieRemoval = 1,
        -- How many zombies it takes to damage a tall fence. Min: -1 Max: 100 Default: 25
        FenceThumpersRequired = 25,
        -- How quickly zombies damage tall fences. Min: 0.01 Max: 100.00 Default: 1.00
        FenceDamageMultiplier = 1.0,
    },
    ZombieConfig = {
        -- Set by the "Zombie Count" population option, or by a custom number here. Insane = 2.5, Very High = 1.6, High = 1.2, Normal = 0.65, Low = 0.15, None = 0.0. Min: 0.00 Max: 4.00 Default: 0.65
        PopulationMultiplier = 0.65,
        -- A multiplier for the desired zombie population at the start of the game. Insane = 3.0, Very High = 2.0, High = 1.5, Normal = 1.0, Low = 0.5, None = 0.0. Min: 0.00 Max: 4.00 Default: 1.00
        PopulationStartMultiplier = 1.0,
        -- A multiplier for the desired zombie population on the peak day. Insane = 3.0, Very High = 2.0, High = 1.5, Normal = 1.0, Low = 0.5, None = 0.0. Min: 0.00 Max: 4.00 Default: 1.50
        PopulationPeakMultiplier = 1.5,
        -- The day when the population reaches its peak. Min: 1 Max: 365 Default: 28
        PopulationPeakDay = 28,
        -- The number of hours that must pass before zombies may respawn in a cell. If 0, spawning is disabled. Min: 0.00 Max: 8760.00 Default: 0.00
        RespawnHours = 0.0,
        -- The number of hours that a chunk must be unseen before zombies may respawn in it. Min: 0.00 Max: 8760.00 Default: 0.00
        RespawnUnseenHours = 0.0,
        -- The fraction of a cell's desired population that may respawn every RespawnHours. Min: 0.00 Max: 1.00 Default: 0.00
        RespawnMultiplier = 0.0,
        -- The number of hours that must pass before zombies migrate  to empty parts of the same cell. If 0, migration is disabled. Min: 0.00 Max: 8760.00 Default: 12.00
        RedistributeHours = 12.0,
        -- The distance a zombie will try to walk towards the last sound it heard. Min: 10 Max: 1000 Default: 100
        FollowSoundDistance = 100,
        -- The size of groups real zombies form when idle. 0 means zombies don't form groups. Groups don't form inside buildings or forest zones. Min: 0 Max: 1000 Default: 20
        RallyGroupSize = 20,
        -- The amount, as a percentage, that zombie groups can vary in size from the default (both larger and smaller).   For example, at 50%% variance with a default group size of 20, groups will vary in size from 10-30. Min: 0 Max: 100 Default: 50
        RallyGroupSizeVariance = 50,
        -- The distance real zombies travel to form groups when idle. Min: 5 Max: 50 Default: 20
        RallyTravelDistance = 20,
        -- The distance between zombie groups. Min: 5 Max: 25 Default: 15
        RallyGroupSeparation = 15,
        -- How close members of a zombie group stay to the group's "leader". Min: 1 Max: 10 Default: 3
        RallyGroupRadius = 3,
        -- Min: 10 Max: 500 Default: 300
        ZombiesCountBeforeDelete = 300,
    },
    MultiplierConfig = {
        -- The rate at which all skills level up. Min: 0.00 Max: 1000.00 Default: 1.00
        Global = 1.0,
        -- When enabled, all skills will use the Global Multiplier.
        GlobalToggle = true,
        -- Rate at which Fitness skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Fitness = 1.0,
        -- Rate at which Strength skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Strength = 1.0,
        -- Rate at which Sprinting skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Sprinting = 1.0,
        -- Rate at which Lightfooted skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Lightfoot = 1.0,
        -- Rate at which Nimble skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Nimble = 1.0,
        -- Rate at which Sneaking skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Sneak = 1.0,
        -- Rate at which Axe skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Axe = 1.0,
        -- Rate at which Long Blunt skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Blunt = 1.0,
        -- Rate at which Short Blunt skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        SmallBlunt = 1.0,
        -- Rate at which Long Blade skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        LongBlade = 1.0,
        -- Rate at which Short Blade skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        SmallBlade = 1.0,
        -- Rate at which Spear skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Spear = 1.0,
        -- Rate at which Maintenance skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Maintenance = 1.0,
        -- Rate at which Carpentry skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Woodwork = 1.0,
        -- Rate at which Cooking skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Cooking = 1.0,
        -- Rate at which Agriculture skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Farming = 1.0,
        -- Rate at which First Aid skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Doctor = 1.0,
        -- Rate at which Electrical skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Electricity = 1.0,
        -- Rate at which Welding skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        MetalWelding = 1.0,
        -- Rate at which Mechanics skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Mechanics = 1.0,
        -- Rate at which Tailoring skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Tailoring = 1.0,
        -- Rate at which Aiming skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Aiming = 1.0,
        -- Rate at which Reloading skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Reloading = 1.0,
        -- Rate at which Fishing skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Fishing = 1.0,
        -- Rate at which Trapping skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Trapping = 1.0,
        -- Rate at which Foraging skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        PlantScavenging = 1.0,
        -- Rate at which Knapping skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        FlintKnapping = 1.0,
        -- Rate at which Masonry skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Masonry = 1.0,
        -- Rate at which Pottery skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Pottery = 1.0,
        -- Rate at which Carving skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Carving = 1.0,
        -- Rate at which Animal Care skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Husbandry = 1.0,
        -- Rate at which Tracking skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Tracking = 1.0,
        -- Rate at which Blacksmithing skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Blacksmith = 1.0,
        -- Rate at which Butchering skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Butchering = 1.0,
        -- Rate at which Glassmaking skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Glassmaking = 1.0,
        -- Rate at which Art skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Art = 1.0,
        -- Rate at which Cleaning skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Cleaning = 1.0,
        -- Rate at which Dancing skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Dancing = 1.0,
        -- Rate at which Meditation skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Meditation = 1.0,
        -- Rate at which Music skill levels up. Min: 0.00 Max: 1000.00 Default: 1.00
        Music = 1.0,
    },
    RVAddon = {
        -- Comma-separated list of vehicle script names (e.g., Base.Van,Base.StepVan,Base.VanSpiffo).
        CustomNormalVehicles = "",
        -- Comma-separated list of bus vehicle script names.
        CustomBusVehicles = "",
        -- Comma-separated list of small vehicle script names.
        CustomSmallVehicles = "",
        -- Comma-separated list of 3x2 caravan/trailer script names.
        Custom3x2Caravan = "",
        -- Comma-separated list of 3x6 caravan/trailer script names.
        Custom3x6Caravan = "",
        -- Comma-separated list of 3x7 empty trailer script names.
        Custom3x7Empty = "",
        -- Comma-separated list of 4x12 colossal vehicle script names.
        Custom4x12colossal = "",
    },
    DAMN = {
        AllowPowerChadSpawns = true,
        AllowPro440Spawns = true,
        AllowWreckyMcChevySpawns = true,
        AllowGreatScottSpawns = false,
        AllowMrBusSpawns = true,
        AllowChonkerSpawns = true,
        AllowCashcowSpawns = true,
        AllowMcBoxySpawns = true,
    },
    HereGoesTheSun = {
        EnableGodRays = true,
        EnableStormMood = true,
        -- Default = Recommended
        -- 1 = Soft
        -- 2 = Recommended
        -- 3 = Night of the Living Dead
        StormMoodPreset = 2,
    },
    RainCleansBlood = {
        -- How many random tiles to clean per in-game minute. Min: 1 Max: 60 Default: 10
        TilesPerMinute = 10,
        -- How heavy the rain or snow must be before blood starts washing away. Higher = needs heavier weather. Min: 0.05 Max: 0.95 Default: 0.25
        WeatherThreshold = 0.25,
        -- Also clean ash left behind by burned corpses.
        AlsoCleanAsh = true,
        -- Also clean blood inside buildings.
        AlsoCleanInside = false,
        -- Also gradually clean blood from vehicles.
        AlsoCleanVehicles = true,
        -- How much blood to remove from vehicles per minute. Min: 0.10 Max: 1.00 Default: 0.10
        VehicleCleanSpeed = 0.1,
        -- Also gradually clean blood and dirt from players' worn clothing.
        AlsoCleanClothes = true,
        -- How much blood and dirt to remove from clothing per minute. Min: 1.00 Max: 10.00 Default: 1.00
        ClothesCleanSpeed = 1.0,
        -- Always clean regardless of weather.
        AlwaysClean = false,
    },
    ZomboidTodo = {
        -- Controls how frequently notebooks, paper, pencils, pens, and erasers appear in containers. Default = Normal
        -- 1 = Insanely Rare
        -- 2 = Extremely Rare
        -- 3 = Rare
        -- 4 = Normal
        -- 5 = Common
        -- 6 = Abundant
        SupplySpawnRate = 4,
        -- When enabled, adding, renaming, or editing todo list entries requires a pencil or pen in the player's inventory.
        RequireWritingTool = true,
        -- When enabled, deleting todo list entries requires an eraser in the player's inventory.
        RequireEraser = false,
    },
    B42Horticulture = {
        -- Adds 'Make Glass Pipe' recipe to 'Magazine: Murano Glass Manual'.
        LearnedRecipe = true,
    },
    JBFireflyOptions = {
        -- Min: 1 Max: 1000 Default: 10
        ticksToSpawn = 10,
        -- Min: 1 Max: 10000 Default: 2
        minSpawn = 2,
        -- Min: 1 Max: 10000 Default: 5
        maxSpawn = 5,
        -- Min: 1 Max: 100000 Default: 100
        maxFireflyInstances = 100,
        -- Min: 5 Max: 150 Default: 50
        spawnArea = 50,
        -- Min: 1 Max: 100 Default: 2
        overSample = 2,
        -- Min: 1 Max: 365 Default: 15
        taperDays = 15,
        -- Min: 0 Max: 360 Default: 180
        startDay = 180,
        -- Min: 0 Max: 360 Default: 245
        endDay = 245,
        hideCantSee = false,
    },
    Text = {
        -- Enable/disable all mechanics related to Music (moodles, traits, interactions, ...).
        DividerMusicNew = true,
        -- Enable/disable all mechanics related to Dancing (moodles, traits, interactions, ...).
        DividerDancingNew = true,
        -- Enable/disable all mechanics related to Meditation and Yoga (moodles, traits, interactions, ...).
        DividerMeditationNew = true,
        -- Enable/disable all mechanics related to Hygiene and Cleaning (moodles, traits, interactions, ...).
        DividerHygiene = true,
        -- Enable/disable all mechanics related to Art (moodles, traits, interactions, ...).
        DividerArt = true,
        -- This is only a line separator, checking it has no effect.
        LSDividerOther = false,
        -- This is only a line separator, checking it has no effect.
        DividerDebug = false,
    },
    LSAmbt = {
        -- Toggle ambitions on or off. Warning: Disabling this will reset all current player progress on ambitions.
        Toggle = true,
        -- The number of in game hours that must pass before a player can toggle on or off a recently activated/deactivated ambition again. Min: 1 Max: 1000 Default: 36
        Cooldown = 36,
        -- The maximum number of incomplete ambitions players can activate and pursue. Passive ambitions are excluded. Min: 1 Max: 100 Default: 1
        MaxInProgress = 1,
        -- The maximum number of ambitions players can activate overall, including both completed and in-progress ambitions. Min: 1 Max: 100 Default: 3
        MaxTotal = 3,
        -- Wether or not resets after editing ambitions' goals apply for players currently working towards them. Forced resets still apply for everyone.
        ResetException = false,
        -- Hidden ambitions won't display clues on how to unlock them.
        HideTips = false,
    },
    Music = {
        -- Controls how strong music related activities are for the musician. Higher values increase their effectiveness on mood and xp gains. Default = Normal
        -- 1 = Low
        -- 2 = Normal
        -- 3 = High
        -- 4 = Very High
        StrengthMultiplier = 2,
        -- Controls how strong the effects of listening to music are. Higher values increase it's effectiveness on mood. Default = Normal
        -- 1 = Low
        -- 2 = Normal
        -- 3 = High
        -- 4 = Very High
        ListeningStrengthMultiplier = 2,
        -- Chance of learning a new song when practicing with an instrument. Music level 2 is required to start learning songs. Default = Normal
        -- 1 = Very Difficult
        -- 2 = Difficult
        -- 3 = Normal
        -- 4 = Easy
        -- 5 = Very Easy
        LearningChance = 3,
        -- Whether or not playing music is physically taxing. Default = Enabled
        -- 1 = Enabled
        -- 2 = Practicing only
        -- 3 = Disabled
        Metabolics = 1,
    },
    Dancing = {
        -- Controls how powerful dancing is. Higher values increase it's effectiveness. Default = Normal
        -- 1 = Low
        -- 2 = Normal
        -- 3 = High
        -- 4 = Very High
        StrengthMultiplier = 2,
    },
    Meditation = {
        -- Controls how powerful meditation is. Higher values increase it's effectiveness. Default = Normal
        -- 1 = Low
        -- 2 = Normal
        -- 3 = High
        -- 4 = Very High
        StrengthMultiplier = 2,
        -- Controls the duration of all mindfulness states. Default = Normal
        -- 1 = Short
        -- 2 = Normal
        -- 3 = Long
        MindfulnessDuration = 2,
        -- How much healing occurs during the Perfect Mindfulness state.
        -- The amount varies depending on your character overall health and game-time settings. Min: 0.00 Max: 10.00 Default: 2.00
        HealFactor = 2.0,
        -- Controls the effectiveness of the mindfulness states bonuses (stress, pain, panic, etc...). Default = Normal
        -- 1 = Weak
        -- 2 = Normal
        -- 3 = Strong
        EffectMultiplier = 2,
        -- Enable/Disable keeping bags and backpacks on during Meditation at lower skill levels.
        KeepBags = false,
    },
    LSMeditation = {
        -- Tick this box to disable levitation at higher levels.
        RemoveLevitation = false,
    },
    Yoga = {
        -- Controls how powerful yoga is. Higher values increases the effectiveness of it's benefits. Default = Normal
        -- 1 = Low
        -- 2 = Normal
        -- 3 = High
        -- 4 = Very High
        StrengthMultiplier = 2,
        -- How exhausted a character has to be before he's unable to practice Yoga. Default = At medium exhaustion (default)
        -- 1 = None (disable the threshold)
        -- 2 = At low exhaustion
        -- 3 = At medium exhaustion (default)
        -- 4 = At high exhaustion
        Exhaustion = 3,
        -- How embarrassed a character has to be before he's unable to practice Yoga. Default = At low embarrassment (default)
        -- 1 = None (disable the threshold)
        -- 2 = At low embarrassment (default)
        -- 3 = At medium embarrassment
        -- 4 = At high embarrassment
        Embarrassment = 2,
        -- Enable/Disable mats and incenses improving Yoga.
        AidObjects = true,
        -- Enable/Disable Yoga mat requirement for practicing the activity.
        RequiresMat = false,
        -- Enable/Disable keeping bags and backpacks on during Yoga.
        KeepBags = false,
        -- How often a character loses balance and falls during difficult Yoga poses (affected by skill). Default = Often (default)
        -- 1 = Never
        -- 2 = Rarely
        -- 3 = Sometimes
        -- 4 = Often (default)
        -- 5 = Very Often
        -- 6 = Two Left Feet (almost always)
        FailChance = 4,
        -- Yoga. Values below 1.0 decrease XP gain. Min: 0.10 Max: 5.00 Default: 1.00
        YogaXPMultiplier = 1.0,
        -- Fitness. Values below 1.0 decrease XP gain. Min: 0.10 Max: 5.00 Default: 1.00
        FitnessXPMultiplier = 1.0,
        -- Nimble. Values below 1.0 decrease XP gain. Min: 0.10 Max: 5.00 Default: 1.00
        NimbleXPMultiplier = 1.0,
    },
    LSHygiene = {
        -- Values below 1.0 decrease the rate, set it to 0 stop the need from increasing. Min: 0.00 Max: 3.00 Default: 1.00
        HygieneNeedMultiplier = 1.0,
        -- Values below 1.0 decrease the rate, set it to 0 stop the need from increasing. Min: 0.00 Max: 3.00 Default: 1.00
        BladderNeedMultiplier = 1.0,
        -- How many survived days it takes for a new survivor to care about hygiene. Default = 4-12 days
        -- 1 = 1-3 days
        -- 2 = 4-12 days
        -- 3 = 2-4 weeks
        -- 4 = 1-3 months
        HygieneNeedExpectationTime = 2,
        -- Whether or not showering and bathing cleans body and facial makeup.
        CleansMakeup = true,
        -- Characters won't mind having others around while bathing or using the toilet.
        NotEmbarrassed = false,
        -- How weak or strong the sickness from low hygiene can be. Default = Mild
        -- 1 = Low
        -- 2 = Mild
        -- 3 = High
        -- 4 = Deadly
        ColdSeverity = 2,
        -- Values below 1.0 lower the chance, set it to 0 to disable the mechanic. Min: 0.00 Max: 3.00 Default: 0.00
        ColdChanceMultiplier = 0.0,
        -- How many survived days it takes for a new survivor to care about their surroundings. Default = 4-12 days
        -- 1 = 1-3 days
        -- 2 = 4-12 days
        -- 3 = 2-4 weeks
        -- 4 = 1-3 months
        CleaningExpectationTime = 2,
        -- Chance for an unskilled character to generate waste during a skill-based activity (e.g. food scraps from cooking with low cooking skill). Default = Normal
        -- 1 = Very Low
        -- 2 = Low
        -- 3 = Normal
        -- 4 = High
        CleaningLitterChance = 3,
    },
    LSArt = {
        -- Whether or not beauty need can drop to negative levels when outdoors.
        BeautyOutdoors = false,
        -- Whether or not negative beauty scores can appear above outdoor tiles (will always appear if ugly outdoors is enabled).
        BeautyShowNegative = false,
        -- The rate at which beauty needs decreases when around ugly or neutral environments. Default = Normal
        -- 1 = Very Slow
        -- 2 = Slow
        -- 3 = Normal
        -- 4 = Fast
        -- 5 = Very Fast
        BeautyNeedDecayRate = 3,
        -- How strong the effects on mood from satisfying or neglecting a character's beauty need are. Default = Normal
        -- 1 = Very Weak
        -- 2 = Weak
        -- 3 = Normal
        -- 4 = Strong
        -- 5 = Very Strong
        BeautyNeedStrength = 3,
        -- Values below 1.0 lower the effect of artworks on beauty score. Min: 0.10 Max: 4.00 Default: 1.00
        ArtworkBeautyMultiplier = 1.0,
    },
    LS = {
        -- Whether or not traits can be lost or gained dynamically.
        DynamicTraits = false,
        -- Whether or not positive traits can be lost when DLT is enabled. 
        --  - Never: will never lose positive traits 
        --  - Always: can lose any lifestyle trait 
        --  - Dynamic only: can only lose traits gained dynamically, will never lose positive traits picked during character creation Default = Never
        -- 1 = Never
        -- 2 = Always
        -- 3 = Dynamic only
        DynamicTraitsReverse = 1,
        -- This is only a line separator, checking it has no effect.
        DividerServer = false,
        -- How often in game time player moddata is updated. Do not change this if you don't know what this is. Default = Set by day length (default)
        -- 1 = Set by day length (default)
        -- 2 = Once per minute
        -- 3 = Per 2 minutes
        -- 4 = Per 5 minutes
        -- 5 = Per 10 minutes
        -- 6 = Per 15 minutes
        -- 7 = Per 30 minutes
        -- 8 = Once per hour
        -- 9 = Per 2 hours
        -- 10 = Per 6 hours
        -- 11 = Per 12 hours
        -- 12 = Once per day
        ModdataUpdate = 1,
        -- How often in game time changes to mood are applied. Only affects passive mood gain/loss (not timed actions) Default = Set by day length (default)
        -- 1 = Set by day length (default)
        -- 2 = Once per minute
        -- 3 = Per 2 minutes
        -- 4 = Per 5 minutes
        -- 5 = Per 10 minutes
        -- 6 = Per 15 minutes
        -- 7 = Per 30 minutes
        -- 8 = Once per hour
        -- 9 = Per 2 hours
        MoodUpdate = 1,
    },
    LSComfort = {
        -- Values below 1.0 decrease the rate, set it to 0 to stop the need from increasing. Min: 0.00 Max: 3.00 Default: 1.00
        ComfortNeedMultiplier = 1.0,
        -- Check to disable comfy chairs and beds giving positive comfort.
        ComfortPositive = false,
        -- Check to stop Lifestyle's Comfort need from impacting vanilla's Discomfortable moodle.
        ComfortNoImpact = false,
    },
    Debug = {
        -- Enabling this will cause other modded moodles to appear above lifestyle moodles.
        MoodlePriority = false,
        -- Enables manual expressions in the admin context menu
        Expressions = false,
        -- Enabling this will make animation names appear above some of the new animations
        DanceAnim = false,
        -- Prints texts. For debugging only.
        LSVerbose = false,
    },
    SOTO = {
        -- Player can earn additional Fitness XP once per game minute while running.
        AddFitXPWhileRun = true,
        -- Possibility to obtain XP boosts while leveling agility skills.
        -- For example, player can obtain Sneaky trait to increase their XP gain for Sneaking skill.
        AgilityTraitsObtainable = true,
        -- Possibility to obtain XP boosts while leveling combat skills.
        -- For example, player can obtain Baseball Player trait to increase their XP gain for Long Blunt skill.
        CombatTraitsObtainable = true,
        -- Possibility to obtain XP boosts while leveling survivalist skills.
        -- For example, player can obtain Forager trait to increase their XP gain for Foraging skill.
        SurvTraitsObtainable = false,
        -- Possibility to obtain XP boosts while leveling crafting skills.
        -- For example, player can obtain Culinary trait to increase their XP gain for Cooking skill.
        CraftTraitsObtainable = false,
        -- Possibility to obtain XP boosts while leveling firearm skills.
        -- For example, player can obtain Shooter trait to increase their XP gain for Aiming skill.
        FirearmTraitsObtainable = true,
        CowardlyRemovable = true,
        -- Should be lower than Max. 1 day = 24 Min: 1 Max: 100000 Default: 168
        CowardlyHoursToRemoveMin = 168,
        -- Should be higher than Min. 1 day = 24 Min: 1 Max: 100000 Default: 336
        CowardlyHoursToRemoveMax = 336,
        -- Should be lower than Max. Min: 1 Max: 100000 Default: 1250
        CowardlyZombiesKilledToRemoveMin = 1250,
        -- Should be higher than Min. Min: 1 Max: 100000 Default: 2500
        CowardlyZombiesKilledToRemoveMax = 2500,
        BraveEarnable = true,
        -- Should be lower than Max. 1 day = 24
        -- x1.2 when starting with Cowardly trait. Min: 1 Max: 100000 Default: 504
        BraveHoursToEarnMin = 504,
        -- Should be higher than Min. 1 day = 24
        -- x1.2 when starting with Cowardly trait. Min: 1 Max: 100000 Default: 840
        BraveHoursToEarnMax = 840,
        -- Should be lower than Max.
        -- x1.2 when starting with Cowardly trait. Min: 1 Max: 100000 Default: 3000
        BraveZombiesKilledToEarnMin = 3000,
        -- Should be higher than Min.
        -- x1.2 when starting with Cowardly trait. Min: 1 Max: 100000 Default: 4500
        BraveZombiesKilledToEarnMax = 4500,
        DesensitizedEarnable = true,
        -- Should be lower than Max. 1 day = 24
        -- x1.2 when starting with Cowardly trait.
        -- x0.8 when starting with Brave trait. Min: 1 Max: 100000 Default: 1176
        DesensitizedHoursToEarnMin = 1176,
        -- Should be higher than Min. 1 day = 24
        -- x1.2 when starting with Cowardly trait.
        -- x0.8 when starting with Brave trait. Min: 1 Max: 100000 Default: 1512
        DesensitizedHoursToEarnMax = 1512,
        -- Should be lower than Max.
        -- x1.2 when starting with Cowardly trait.
        -- x0.8 when starting with Brave trait. Min: 1 Max: 100000 Default: 6000
        DesensitizedZombiesKilledToEarnMin = 6000,
        -- Should be higher than Min.
        -- x1.2 when starting with Cowardly trait.
        -- x0.8 when starting with Brave trait. Min: 1 Max: 100000 Default: 9000
        DesensitizedZombiesKilledToEarnMax = 9000,
        PacifistRemovable = true,
        -- Should be lower than Max. 1 day = 24 Min: 1 Max: 100000 Default: 672
        PacifistHoursToRemoveMin = 672,
        -- Should be higher than Min. 1 day = 24 Min: 1 Max: 100000 Default: 1008
        PacifistHoursToRemoveMax = 1008,
        -- Should be lower than Max. Min: 1 Max: 100000 Default: 1500
        PacifistZombiesKilledToRemoveMin = 1500,
        -- Should be higher than Min. Min: 1 Max: 100000 Default: 2500
        PacifistZombiesKilledToRemoveMax = 2500,
        -- Any weapon skill but Maintenance and Reloading. Min: 0 Max: 10 Default: 7
        PacifistSkillLvlToRemove = 7,
        SmokerRemovable = true,
        -- Should be lower than Max. 1 day = 24 Min: 1 Max: 100000 Default: 672
        SmokerHoursToRemoveMin = 672,
        -- Should be higher than Min. 1 day = 24 Min: 1 Max: 100000 Default: 768
        SmokerHoursToRemoveMax = 768,
        AlcoholicRemovable = true,
        -- Should be lower than Max. 1 day = 24 Min: 1 Max: 100000 Default: 1032
        AlcoholicHoursToRemoveMin = 1032,
        -- Should be higher than Min. 1 day = 24 Min: 1 Max: 100000 Default: 1128
        AlcoholicHoursToRemoveMax = 1128,
        SundayDriverRemovable = true,
        -- Should be lower than Max. 1 day = 24 Min: 1 Max: 100000 Default: 60
        SundayDriverHoursToRemoveMin = 60,
        -- Should be higher than Min. 1 day = 24 Min: 1 Max: 100000 Default: 80
        SundayDriverHoursToRemoveMax = 80,
        AllThumbsRemovable = true,
        -- (transferring time) Min: 1 Max: 100000 Default: 37500
        AllThumbsValueToRemove = 37500,
        DisorganizedRemovable = true,
        -- (transferring weight) Min: 1 Max: 100000 Default: 37500
        DisorganizedValueToRemove = 37500,
        GracefulEarnable = true,
        ClumsyRemovable = true,
        InconspicuousEarnable = true,
        ConspicuousRemovable = true,
    },
    TakeABathAndShower = {
        -- This checkbox option does nothing itself.
        GeneralSection = false,
        -- Whether has a water temperature concept to shower and bath. 
        --  If False, you will no longer be able to get the warming to body effects of hot water or the stress relief effects.
        WaterTemperatureConcept = true,
        -- This is the amount of water remaining in the bathtub faucet after a water outage. <LINE> By making this value higher than the amount of taking bath water consumed, you will be able to take a bath in the first house you visit after the water outage. Min: 0 Max: 1000 Default: 100
        RemainTubFaucetWater = 100,
        -- This is the amount of water remaining in the shower faucet after a water outage. <LINE> By making this value higher than the amount of taking shower water consumed, you will be able to take a shower in the first house you visit after the water outage. Min: 0 Max: 1000 Default: 20
        RemainShowerFaucetWater = 20,
        -- The chance of body shampoo spawning. Default = Rare
        -- 1 = None
        -- 2 = Extremely Rare
        -- 3 = Rare
        -- 4 = Normal
        -- 5 = Common
        -- 6 = Abundant
        BathItemSpawnChance = 3,
        -- The chance of bath salt spawning. Default = Extremely Rare
        -- 1 = None
        -- 2 = Extremely Rare
        -- 3 = Rare
        -- 4 = Normal
        -- 5 = Common
        -- 6 = Abundant
        BathSaltSpawnChance = 2,
        -- This checkbox option does nothing itself.
        TubFluidContainerSection = false,
        -- The amount of water that can be stored in a bathtub. 
        --  <PUSHRGB:1,0.5,0.5> Note: This is separate from the amount of water remaining in the faucet when shut out of the water supply. <POPRGB> Min: 100 Max: 1000 Default: 200
        TubWaterCapacity = 200,
        -- If you placed bathtub to outdoors, you can collect rainwater. But you cannot use that water for plumbing.
        TubRainCollect = true,
        -- When you bathing, the water becomes tainted by the dirt washed off your body.
        TubWaterGetDirty = true,
        -- If you have electricity, you can reheat the bath water.
        EnableReheat = true,
        -- Whether to consider all fluid types when check for fluid containers plumbed into baths and showers. If disabled, only fluid containers containing water will be considered.
        AvailableAllFluid = false,
        -- This checkbox option does nothing itself.
        BathAndShowerSection = false,
        -- The amount of water consumed when washing blood, dirt, and grime from your body during a bath. This is a relative value based on the total amount removed. If you want to disable water consumption, set it to 0. Min: 0.00 Max: 1.00 Default: 0.80
        WashInBathConsumeWater = 0.8,
        -- The amount of water needed to take a shower. Min: 0 Max: 200 Default: 80
        ShowerConsumeWater = 80,
        -- Disable the increase discomfort, boredom, and unhappiness that comes from bathing with wearing clothes or in bad condition bathwater (wrong temperature or dirty).
        DisableNegativeEffectsOfBathing = false,
        -- Disable the increased stress caused by someone (includ zombies) seen at you while bathing.
        DisableFeelingStressByGaze = false,
        -- This checkbox option does nothing itself.
        BodyGrimeSection = false,
        -- Enable Body Grime functions. If this to False, all settings below this will be disabled.
        EnableBodyGrime = true,
        -- Displays a moodle that increases in severity for every 25 Body Grime accumulated. <LINE> <PUSHRGB:1,0.5,0.5> It will not work if Moodle Framework Mod is not installed!<POPRGB>
        EnableBodyGrimeMoodle = true,
        -- The base amount of Grime that accumulates for your body every hour without you doing anything. Min: 0.00 Max: 100.00 Default: 0.80
        BodyGrimeIncreasedBase = 0.8,
        -- If there is more blood on your body than this value, it will accumulate on the body as Grime. Min: 0 Max: 100 Default: 30
        BloodToGrimeThreshold = 30,
        -- If there is more dirt on your body than this value, it will accumulate on the body as Grime. Min: 0 Max: 100 Default: 30
        DirtToGrimeThreshold = 30,
        -- A multiplier on how amount blood and dirt over the threshold will accumulate as grime. <LINE> This is calculated by total blood or dirt stains on full body, not by part, and the maximum value is 1, not 100. <LINE> If you set this value to 3, you will accumulate 1.5 additional grime every hour if you have 50 blood on your body. Min: 0.00 Max: 100.00 Default: 1.00
        BloodAndDirtMultiplier = 1.0,
        -- If you have too much Grime, you will feel discomfort.
        GrimeDiscomfort = true,
        -- If you have too much Grime, you will feel a slight noxious smell.
        GrimeNoxiousSmell = true,
        -- Amount of grime removed in Vanilla Wash Self. Min: 0 Max: 10 Default: 2
        WashSelfRemoveGrimeAmount = 2,
    },
    STA_PryOpen = {
        -- Toggle wheather prying gets easier with consecutive failures. (1%% bonus up to 15%%)
        PryEnablePity = false,
        -- Base success chance before modifiers. Min: 0.01 Max: 1.00 Default: 0.25
        PryChanceBase = 0.25,
        -- Success chance bonus per Strength level. Min: 0.00 Max: 1.00 Default: 0.03
        PryBonusSkillStrength = 0.03,
        -- Success chance bonus per Carpentry level (only for Sandbox_STA_PryOpenndard doors and windows). Min: 0.00 Max: 1.00 Default: 0.03
        PryBonusSkillCarpentry = 0.03,
        -- Success chance bonus per Blacksmith level (only for security doors and garage doors). Min: 0.00 Max: 1.00 Default: 0.03
        PryBonusSkillBlacksmith = 0.03,
        -- Success chance bonus per Mechanics level (only for vehicle doors and trunks). Min: 0.00 Max: 1.00 Default: 0.03
        PryBonusSkillMechanics = 0.03,
        -- Success chance bonus for the Burglar trait. Min: 0.00 Max: 1.00 Default: 0.15
        PryBonusTraitBurglar = 0.15,
        -- Time required reduction per Nimble level. Min: 0.00 Max: 5.00 Default: 0.20
        PryBonusSkillNimble = 0.2,
        -- Time required reduction for Dextrous trait. Min: 0.00 Max: 5.00 Default: 1.00
        PryBonusTraitDextrous = 1.0,
        -- Toggle whether Players can pry open building doors.
        PryEnableBuilding = true,
        -- Minimum Strength level at which Players can pry open building doors. Min: 0 Max: 10 Default: 3
        PryLevelBuilding = 3,
        -- Success chance multiplier for building doors (applied after bonuses). Min: 0.01 Max: 5.00 Default: 1.00
        PryChanceMultiplierBuilding = 1.0,
        -- Seconds required to attempt prying open building doors. Min: 1 Max: 30 Default: 8
        PryTimeBuilding = 8,
        -- Toggle whether Players can pry open building windows.
        PryEnableWindow = true,
        -- Minimum Strength level at which Players can pry open building windows. Min: 0 Max: 10 Default: 2
        PryLevelWindow = 2,
        -- Success chance multiplier for building windows (applied after bonuses). Min: 0.01 Max: 5.00 Default: 1.10
        PryChanceMultiplierWindow = 1.1,
        -- Seconds required to attempt prying open building windows. Min: 1 Max: 30 Default: 6
        PryTimeWindow = 6,
        -- Toggle whether Players can pry open garage doors.
        PryEnableGarage = true,
        -- Minimum Strength level at which Players can pry open garage doors. Min: 0 Max: 10 Default: 6
        PryLevelGarage = 6,
        -- Success chance multiplier for garage doors (applied after bonuses). Min: 0.01 Max: 5.00 Default: 0.85
        PryChanceMultiplierGarage = 0.85,
        -- Seconds required to attempt prying open garage doors. Min: 1 Max: 30 Default: 10
        PryTimeGarage = 10,
        -- Toggle whether Players can pry open security doors.
        PryEnableSecure = true,
        -- Minimum Strength level at which Players can pry open security doors. Min: 0 Max: 10 Default: 8
        PryLevelSecure = 8,
        -- Success chance multiplier for security doors (applied after bonuses). Min: 0.01 Max: 5.00 Default: 0.80
        PryChanceMultiplierSecure = 0.8,
        -- Seconds required to attempt prying open security doors. Min: 1 Max: 30 Default: 14
        PryTimeSecure = 14,
        -- Toggle whether Players can pry open vehicle doors.
        PryEnableVehicle = true,
        -- Minimum Strength level at which Players can pry open vehicle doors. Min: 0 Max: 10 Default: 3
        PryLevelVehicle = 3,
        -- Success chance multiplier for vehicle doors (applied after bonuses). Min: 0.01 Max: 5.00 Default: 1.00
        PryChanceMultiplierVehicle = 1.0,
        -- Seconds required to attempt prying open vehicle doors. Min: 1 Max: 30 Default: 10
        PryTimeVehicle = 10,
        -- Toggle whether Players can pry open vehicle trunks.
        PryEnableTrunk = true,
        -- Minimum Strength level at which Players can pry open vehicle trunks. Min: 0 Max: 10 Default: 2
        PryLevelTrunk = 2,
        -- Success chance multiplier for vehicle trunks (applied after bonuses). Min: 0.01 Max: 5.00 Default: 1.05
        PryChanceMultiplierTrunk = 1.05,
        -- Seconds required to attempt prying open vehicle trunks. Min: 1 Max: 30 Default: 8
        PryTimeTrunk = 8,
        -- Percent chance a building window shatters after failing to it pry open. Min: 0.00 Max: 1.00 Default: 0.30
        PryChanceBreakWindow = 0.3,
        -- Percent chance a vehicle window shatters after failing to pry open the door. Min: 0.00 Max: 1.00 Default: 0.20
        PryChanceBreakVehicleWindow = 0.2,
        -- Percent chance a vehicle door lock breaks after failing to pry open the door. Min: 0.00 Max: 1.00 Default: 0.15
        PryChanceBreakVehicleLock = 0.15,
        -- Percent chance of hand injury occurring after failing to pry something open. Min: 0.00 Max: 1.00 Default: 0.08
        PryChanceInjury = 0.08,
        -- Injury chance bonus or penalty for the Thick-Skinned or Thin-Skinned traits. Min: 0.00 Max: 1.00 Default: 0.05
        PryBonusTraitSkin = 0.05,
        -- Percent chance that hand injury is a scratch. Min: 0.00 Max: 1.00 Default: 0.65
        PryChanceInjurySeverity01 = 0.65,
        -- Percent chance that hand injury is a laceration. Min: 0.00 Max: 1.00 Default: 0.30
        PryChanceInjurySeverity02 = 0.3,
        -- Percent chance that hand injury is a deep wound. Min: 0.00 Max: 1.00 Default: 0.05
        PryChanceInjurySeverity03 = 0.05,
        -- How many tiles the crowbar noise travels to attract zomboids. Min: 5 Max: 100 Default: 15
        PryNoiseRadius = 15,
        -- How many tiles the crowbar noise is reduced per Sneaking level. Min: 0.00 Max: 10.00 Default: 0.50
        PryBonusSkillSneak = 0.5,
        -- Toggle disabling alarms after successfully prying something open.
        PryEnableAlarmSuccess = true,
        -- Enable car/building alarms when the Alarm Chance %% is triggered (alarms are otherwise only trigger if the Alarm Chance %% is triggered and the vehicle/building alarm was previously enabled).
        PryEnableAlarmForce = true,
        -- Percent chance of an alarm being triggered after failing to pry something open. Min: 0.00 Max: 1.00 Default: 0.12
        PryChanceAlarm = 0.12,
        -- Alarm chance reduction per level of Electrical. Min: 0.00 Max: 1.00 Default: 0.01
        PryBonusSkillElectricity = 0.01,
        -- Values for the base chance of items. <LINE>Min: 0.00 Max: 5.00 <LINE>Format as 'Base.Item:1.0' <LINE>Seperate items with ';'
        PryToolItemsList = "",
        -- Values for the base chance of item tags. <LINE>Min: 0.00 Max: 5.00 <LINE>Format as 'base:tag:1.0' <LINE>Seperate tags with ';'
        PryToolTagsList = "base:crowbar:1.0;",
        -- How security doors are unlocked. <LINE><LINE>Vanilla: Security doors will remain locked after being opened, meaning they will need to be pryed open again if they close behind you. <LINE>Full Unlock: Security doors will fully unlock and act as regular interior doors when pryed open. Default = Vanilla
        -- 1 = Vanilla
        -- 2 = Full Unlock
        SecurityDoorHandling = 1,
    },
    FRUsedCars = {
        LowConPartsFall = true,
        PartFallsWithParent = true,
    },
    bikinitools = {
        EnableGetKeyContext = false,
        EnableOpenSesame = false,
        EnableVehicleRemover = false,
        EnableCellVehicleRemover = false,
        EnableRepairContext = false,
        EnableSkinSwitcher = false,
        EnableVehicleSpawner = false,
        EnableTrunkUnlocker = false,
        EnableGravelBuddy = true,
        EnableGardener = true,
        AllowTYLPlantRemoval = true,
        EnableLumberjack = true,
        EnableFarmer = true,
        EnableContainerUnloader = true,
        EnableHomeWrecker = false,
        EnableCorpseStacker = true,
        EnableVehicleItemHide = true,
    },
    BCR = {
        -- How many zombie kills before earning a reward. <LINE><LINE> <RGB:0.6,1.0,0.2> Lower = Faster rewards <LINE> <RGB:1.0,0.6,0.2> Higher = Slower rewards Min: 2 Max: 10000 Default: 1000
        BodyCount = 1000,
        -- Allow earning positive traits as rewards. <LINE><LINE> <RGB:0.8,0.8,0.8> Default: Enabled
        enablePositiveTraits = true,
        -- Allow removing negative traits as rewards. <LINE><LINE> <RGB:0.8,0.8,0.8> Default: Disabled
        enableNegativeTraits = true,
        -- Grant rewards for kills made before installing the mod. <LINE><LINE> <RGB:1.0,0.6,0.2> WARNING: High body counts may grant many rewards at once! <LINE><LINE> <RGB:0.8,0.8,0.8> Default: Disabled
        grandMissedOpportunities = false,
        -- What comes first when you hit a milestone? <LINE><LINE> <RGB:0.6,1.0,0.2> Gain First: Earn positive traits before removing negative ones <LINE> <RGB:1.0,0.6,0.2> Lose First: Remove negative traits before gaining positive ones <LINE> <RGB:0.8,0.3,1.0> Random: Keep things spicy! Default = Gain First
        -- 1 = Gain First
        -- 2 = Lose First
        -- 3 = Random
        rewardPriority = 1,
        -- How the kill requirement grows between milestones. <LINE><LINE> <RGB:0.5,0.8,1.0> __________________________ <LINE> <RGB:1.0,0.85,0.4> LINEAR (BodyCount = 1,000): <LINE> <RGB:0.8,0.8,0.8>   Milestone #1  = 1,000 <LINE>   Milestone #2  = 2,000 <LINE>   Milestone #3  = 3,000 <LINE>   Milestone #5  = 5,000 <LINE>   Milestone #10 = 10,000 <LINE><LINE> <RGB:0.6,1.0,0.2> PROGRESSIVE x1.0 (BodyCount = 1,000): <LINE> <RGB:0.8,0.8,0.8>   Milestone #1  = 1,000 <LINE>   Milestone #2  = 3,000 <LINE>   Milestone #3  = 6,000 <LINE>   Milestone #5  = 15,000 <LINE>   Milestone #10 = 55,000 <LINE> <RGB:0.5,0.8,1.0> __________________________ Default = Linear (constant)
        -- 1 = Linear (constant)
        -- 2 = Progressive (increasing)
        MilestoneScaling = 1,
        -- Controls how steeply the kill requirement grows in Progressive mode. <LINE><LINE> <RGB:0.5,0.8,1.0> __________________________ <LINE> <RGB:0.8,0.8,0.8> Examples with BodyCount = 1,000: <LINE> <RGB:0.5,0.8,1.0> __________________________ <LINE><LINE> <RGB:0.6,1.0,0.2> Factor 0.5 (Gentle): <LINE> <RGB:0.8,0.8,0.8>   #1 = 1,000  |  #2 = 2,500  |  #3 = 4,500 <LINE>   #5 = 10,000  |  #10 = 32,500 <LINE><LINE> <RGB:1.0,0.85,0.4> Factor 1.0 (Default): <LINE> <RGB:0.8,0.8,0.8>   #1 = 1,000  |  #2 = 3,000  |  #3 = 6,000 <LINE>   #5 = 15,000  |  #10 = 55,000 <LINE><LINE> <RGB:1.0,0.6,0.2> Factor 2.0 (Extreme): <LINE> <RGB:0.8,0.8,0.8>   #1 = 1,000  |  #2 = 4,000  |  #3 = 9,000 <LINE>   #5 = 25,000  |  #10 = 100,000 <LINE> <RGB:0.5,0.8,1.0> __________________________ <LINE><LINE> <RGB:1.0,0.5,0.5> Only applies when Milestone Scaling is set to Progressive. Min: 0.10 Max: 2.00 Default: 0.50
        ProgressiveScalingFactor = 0.5,
        -- <RGB:0.6,1.0,0.2> [+] POSITIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow earning this trait as a reward. <LINE><LINE> <RGB:0.7,0.7,0.7> Rarity: Common
        allow_SPEED_DEMON = true,
        -- <RGB:0.6,1.0,0.2> [+] POSITIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow earning this trait as a reward. <LINE><LINE> <RGB:0.7,0.7,0.7> Rarity: Common
        allow_NIGHT_VISION = true,
        -- <RGB:0.6,1.0,0.2> [+] POSITIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow earning this trait as a reward. <LINE><LINE> <RGB:0.7,0.7,0.7> Rarity: Common
        allow_DEXTROUS = true,
        -- <RGB:0.6,1.0,0.2> [+] POSITIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow earning this trait as a reward. <LINE><LINE> <RGB:0.7,0.7,0.7> Rarity: Common
        allow_FAST_READER = true,
        -- <RGB:0.6,1.0,0.2> [+] POSITIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow earning this trait as a reward. <LINE><LINE> <RGB:0.7,0.7,0.7> Rarity: Common
        allow_INVENTIVE = true,
        -- <RGB:0.6,1.0,0.2> [+] POSITIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow earning this trait as a reward. <LINE><LINE> <RGB:0.7,0.7,0.7> Rarity: Common
        allow_LIGHT_EATER = true,
        -- <RGB:0.6,1.0,0.2> [+] POSITIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow earning this trait as a reward. <LINE><LINE> <RGB:0.7,0.7,0.7> Rarity: Common
        allow_LOW_THIRST = true,
        -- <RGB:0.6,1.0,0.2> [+] POSITIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow earning this trait as a reward. <LINE><LINE> <RGB:0.7,0.7,0.7> Rarity: Common
        allow_OUTDOORSMAN = true,
        -- <RGB:0.6,1.0,0.2> [+] POSITIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow earning this trait as a reward. <LINE><LINE> <RGB:0.7,0.7,0.7> Rarity: Common
        allow_NEEDS_LESS_SLEEP = true,
        -- <RGB:0.6,1.0,0.2> [+] POSITIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow earning this trait as a reward. <LINE><LINE> <RGB:0.6,1.0,0.2> Rarity: Uncommon
        allow_IRON_GUT = true,
        -- <RGB:0.6,1.0,0.2> [+] POSITIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow earning this trait as a reward. <LINE><LINE> <RGB:0.6,1.0,0.2> Rarity: Uncommon
        allow_ADRENALINE_JUNKIE = true,
        -- <RGB:0.6,1.0,0.2> [+] POSITIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow earning this trait as a reward. <LINE><LINE> <RGB:0.6,1.0,0.2> Rarity: Uncommon
        allow_EAGLE_EYED = true,
        -- <RGB:0.6,1.0,0.2> [+] POSITIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow earning this trait as a reward. <LINE><LINE> <RGB:0.6,1.0,0.2> Rarity: Uncommon
        allow_GRACEFUL = true,
        -- <RGB:0.6,1.0,0.2> [+] POSITIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow earning this trait as a reward. <LINE><LINE> <RGB:0.6,1.0,0.2> Rarity: Uncommon
        allow_INCONSPICUOUS = true,
        -- <RGB:0.6,1.0,0.2> [+] POSITIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow earning this trait as a reward. <LINE><LINE> <RGB:0.6,1.0,0.2> Rarity: Uncommon
        allow_NUTRITIONIST = true,
        -- <RGB:0.6,1.0,0.2> [+] POSITIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow earning this trait as a reward. <LINE><LINE> <RGB:0.6,1.0,0.2> Rarity: Uncommon
        allow_ORGANIZED = true,
        -- <RGB:0.6,1.0,0.2> [+] POSITIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow earning this trait as a reward. <LINE><LINE> <RGB:0.6,1.0,0.2> Rarity: Uncommon
        allow_RESILIENT = true,
        -- <RGB:0.6,1.0,0.2> [+] POSITIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow earning this trait as a reward. <LINE><LINE> <RGB:0.4,0.6,1.0> Rarity: Rare
        allow_FAST_HEALER = true,
        -- <RGB:0.6,1.0,0.2> [+] POSITIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow earning this trait as a reward. <LINE><LINE> <RGB:0.4,0.6,1.0> Rarity: Rare
        allow_FAST_LEARNER = true,
        -- <RGB:0.6,1.0,0.2> [+] POSITIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow earning this trait as a reward. <LINE><LINE> <RGB:0.4,0.6,1.0> Rarity: Rare
        allow_KEEN_HEARING = true,
        -- <RGB:0.6,1.0,0.2> [+] POSITIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow earning this trait as a reward. <LINE><LINE> <RGB:0.8,0.3,1.0> Rarity: Very Rare
        allow_THICK_SKINNED = true,
        -- <RGB:1.0,0.4,0.4> [-] NEGATIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow removing this trait as a reward. <LINE><LINE> <RGB:0.7,0.7,0.7> Rarity: Common
        allow_HIGH_THIRST = true,
        -- <RGB:1.0,0.4,0.4> [-] NEGATIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow removing this trait as a reward. <LINE><LINE> <RGB:0.7,0.7,0.7> Rarity: Common
        allow_SUNDAY_DRIVER = true,
        -- <RGB:1.0,0.4,0.4> [-] NEGATIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow removing this trait as a reward. <LINE><LINE> <RGB:0.7,0.7,0.7> Rarity: Common
        allow_ALL_THUMBS = true,
        -- <RGB:1.0,0.4,0.4> [-] NEGATIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow removing this trait as a reward. <LINE><LINE> <RGB:0.7,0.7,0.7> Rarity: Common
        allow_CLUMSY = true,
        -- <RGB:1.0,0.4,0.4> [-] NEGATIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow removing this trait as a reward. <LINE><LINE> <RGB:0.7,0.7,0.7> Rarity: Common
        allow_COWARDLY = true,
        -- <RGB:1.0,0.4,0.4> [-] NEGATIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow removing this trait as a reward. <LINE><LINE> <RGB:0.7,0.7,0.7> Rarity: Common
        allow_SLOW_READER = true,
        -- <RGB:1.0,0.4,0.4> [-] NEGATIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow removing this trait as a reward. <LINE><LINE> <RGB:0.6,1.0,0.2> Rarity: Uncommon
        allow_SLOW_HEALER = true,
        -- <RGB:1.0,0.4,0.4> [-] NEGATIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow removing this trait as a reward. <LINE><LINE> <RGB:0.6,1.0,0.2> Rarity: Uncommon
        allow_WEAK_STOMACH = true,
        -- <RGB:1.0,0.4,0.4> [-] NEGATIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow removing this trait as a reward. <LINE><LINE> <RGB:0.6,1.0,0.2> Rarity: Uncommon
        allow_SMOKER = true,
        -- <RGB:1.0,0.4,0.4> [-] NEGATIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow removing this trait as a reward. <LINE><LINE> <RGB:0.6,1.0,0.2> Rarity: Uncommon
        allow_AGORAPHOBIC = true,
        -- <RGB:1.0,0.4,0.4> [-] NEGATIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow removing this trait as a reward. <LINE><LINE> <RGB:0.6,1.0,0.2> Rarity: Uncommon
        allow_CLAUSTROPHOBIC = true,
        -- <RGB:1.0,0.4,0.4> [-] NEGATIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow removing this trait as a reward. <LINE><LINE> <RGB:0.6,1.0,0.2> Rarity: Uncommon
        allow_CONSPICUOUS = true,
        -- <RGB:1.0,0.4,0.4> [-] NEGATIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow removing this trait as a reward. <LINE><LINE> <RGB:0.6,1.0,0.2> Rarity: Uncommon
        allow_HEARTY_APPETITE = true,
        -- <RGB:1.0,0.4,0.4> [-] NEGATIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow removing this trait as a reward. <LINE><LINE> <RGB:0.6,1.0,0.2> Rarity: Uncommon
        allow_PACIFIST = true,
        -- <RGB:1.0,0.4,0.4> [-] NEGATIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow removing this trait as a reward. <LINE><LINE> <RGB:0.6,1.0,0.2> Rarity: Uncommon
        allow_PRONE_TO_ILLNESS = true,
        -- <RGB:1.0,0.4,0.4> [-] NEGATIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow removing this trait as a reward. <LINE><LINE> <RGB:0.6,1.0,0.2> Rarity: Uncommon
        allow_NEEDS_MORE_SLEEP = true,
        -- <RGB:1.0,0.4,0.4> [-] NEGATIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow removing this trait as a reward. <LINE><LINE> <RGB:0.4,0.6,1.0> Rarity: Rare
        allow_ASTHMATIC = true,
        -- <RGB:1.0,0.4,0.4> [-] NEGATIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow removing this trait as a reward. <LINE><LINE> <RGB:0.4,0.6,1.0> Rarity: Rare
        allow_HEMOPHOBIC = true,
        -- <RGB:1.0,0.4,0.4> [-] NEGATIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow removing this trait as a reward. <LINE><LINE> <RGB:0.4,0.6,1.0> Rarity: Rare
        allow_DISORGANIZED = true,
        -- <RGB:1.0,0.4,0.4> [-] NEGATIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow removing this trait as a reward. <LINE><LINE> <RGB:0.4,0.6,1.0> Rarity: Rare
        allow_SLOW_LEARNER = true,
        -- <RGB:1.0,0.4,0.4> [-] NEGATIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow removing this trait as a reward. <LINE><LINE> <RGB:0.8,0.3,1.0> Rarity: Very Rare
        allow_ILLITERATE = true,
        -- <RGB:1.0,0.4,0.4> [-] NEGATIVE TRAIT <LINE><LINE> <RGB:0.8,0.8,0.8> Allow removing this trait as a reward. <LINE><LINE> <RGB:0.8,0.3,1.0> Rarity: Very Rare
        allow_THIN_SKINNED = true,
    },
    InjuredZombiesStumble = {
        -- Min: 0 Max: 100 Default: 40
        BaseChance = 40,
        -- Min: 10 Max: 90 Default: 70
        MinHealthPercent = 70,
        -- Min: 0 Max: 500 Default: 25
        MinCooldown = 25,
        -- Min: 0 Max: 500 Default: 60
        MaxCooldown = 60,
    },
    AshboroCigaretteVending = {
        -- Allow Ashboro cigarette vending machines to appear beside existing vending machines.
        EnableWorldSpawns = true,
        -- Percent chance for an Ashboro machine to spawn beside a valid vending machine. Min: 0 Max: 100 Default: 35
        BaseSpawnChance = 35,
        -- Percent chance to replace the original vending machine if no beside spawn is placed. Min: 0 Max: 100 Default: 0
        ReplaceChance = 0,
        -- Percent chance used when a matching bar location is detected. Min: 0 Max: 100 Default: 55
        BarSpawnChance = 55,
        -- Percent chance used when a matching liquor store location is detected. Min: 0 Max: 100 Default: 65
        LiquorSpawnChance = 65,
        -- Percent chance used when a matching gas station location is detected. Min: 0 Max: 100 Default: 45
        GasSpawnChance = 45,
        -- Percent chance used when a matching convenience store location is detected. Min: 0 Max: 100 Default: 45
        ConvenienceSpawnChance = 45,
        -- Percent chance used when a matching market location is detected. Min: 0 Max: 100 Default: 40
        MarketSpawnChance = 40,
        -- Percent chance used when a matching grocery location is detected. Min: 0 Max: 100 Default: 35
        GrocerySpawnChance = 35,
        -- Percent chance used when a matching store location is detected. Min: 0 Max: 100 Default: 30
        StoreSpawnChance = 30,
    },
    ImmersiveSuicide = {
        -- When checked, player will always become a zombie after suicide, even if not infected.
        ForceZombification = false,
        -- Do you want a suicide confirmation popup to appear before performing a suicide?
        ShowConfirmationModal = true,
    },
    ProximityInventory = {
        -- Enable this if you want the Proximity Inventory to work only on zombies
        ZombieOnly = false,
    },
    SaucedCarts = {
        -- Enable or disable the SaucedCarts mod.
        EnableMod = true,
        -- EXPERIMENTAL — off by default. Allows loading and unloading corpses to/from carts via grapple + right-click 'Load into Cart'. Includes vanilla-faithful rot accounting (corpses age in the cart, despawn at the sandbox HoursForCorpseRemoval threshold). Still being tested in MP — opt in if you want to try it; expect rough edges.
        EnableCorpseStorage = false,
        -- How often carts spawn in the world. 100 = default, 0 = no spawns, 200 = double spawns. Min: 0 Max: 500 Default: 100
        SpawnRate = 100,
        -- Multiplier for cart capacity. 100 = default, 50 = half capacity, 200 = double capacity. Min: 25 Max: 400 Default: 100
        CapacityMultiplier = 100,
        -- Multiplier for cart durability. 100 = default, 50 = breaks faster, 200 = lasts longer. Min: 25 Max: 400 Default: 100
        DurabilityMultiplier = 100,
        -- Maximum number of carts that can spawn in a single building. 1 = default, 5 = max. Min: 1 Max: 5 Default: 1
        MaxCartsPerBuilding = 1,
        -- Percentage of item weight reduced when stored in carts. 95 = items weigh 5%% of normal (default), 100 = items weigh nothing, 0 = no reduction. Min: 0 Max: 99 Default: 95
        WeightReduction = 95,
        -- Movement speed penalty when pushing carts. 100 = default, 0 = no penalty, 200 = double penalty. Min: 0 Max: 200 Default: 100
        SpeedPenaltyMultiplier = 100,
        -- How much condition is restored per repair. 100 = default, 200 = double repair, 50 = half repair. Min: 25 Max: 400 Default: 100
        RepairAmountMultiplier = 100,
        -- How long repairs take. 100 = default, 50 = faster repairs, 200 = slower repairs. Min: 25 Max: 400 Default: 100
        RepairTimeMultiplier = 100,
        -- When enabled, Maintenance skill improves repair effectiveness and speed, and awards XP.
        MaintenanceSkillBonus = true,
        -- Enable detailed debug logging. Disable for better performance when playing with PZ debug mode on.
        EnableDebugLogs = false,
        -- When enabled, carts only spawn in buildings PZ flags as shops (BuildingDef.isShop). Reduces surprise spawns at the cost of some legitimate spawn locations. Combined with the always-on residential/outdoor filter.
        StrictShopOnly = false,
    },
    TrashAndCorpses = {
        -- Controls spawn frequency for trash, corpses, and glass together. 'Rare' is the vanilla-feeling preset with visible trash/glass and occasional corpses. Use 'Advanced Spawn Control' for individual control. Default = Rare
        -- 1 = None
        -- 2 = Very Rare
        -- 3 = Rare
        -- 4 = Normal
        -- 5 = Common
        -- 6 = Very Common
        SpawnRate = 3,
        -- Enable or disable corpse spawning. WARNING: Corpses do NOT work in Multiplayer and will cause harmless error messages. Only enable for Singleplayer! Default = Enabled (SP Only)
        -- 1 = Disabled
        -- 2 = Enabled (SP Only)
        CorpseType = 2,
        -- How much loot spawns inside trash piles. Default = Normal
        -- 1 = None
        -- 2 = Very Rare
        -- 3 = Rare
        -- 4 = Normal
        -- 5 = Common
        -- 6 = Very Common
        LootDensity = 4,
        -- If enabled, trash piles spawn with no loot containers at all (pure decoration).
        TrashDecorativeOnly = false,
        -- Controls where trash and corpses are allowed to spawn. Default = Everywhere
        -- 1 = Everywhere
        -- 2 = Cities Only
        -- 3 = Indoors Only
        -- 4 = Outdoors Only
        LocationFilter = 1,
        -- Enable individual control over corpse, trash, and glass spawn rates. When enabled, overrides 'Overall Spawn Rate'.
        AdvancedSpawnControl = false,
        -- Only active when 'Advanced Spawn Control' is enabled. Controls how often corpses spawn. Default = Normal
        -- 1 = None
        -- 2 = Very Rare
        -- 3 = Rare
        -- 4 = Normal
        -- 5 = Common
        -- 6 = Very Common
        CorpseSpawnRate = 4,
        -- Only active when 'Advanced Spawn Control' is enabled. Controls how often trash piles spawn. Default = Normal
        -- 1 = None
        -- 2 = Very Rare
        -- 3 = Rare
        -- 4 = Normal
        -- 5 = Common
        -- 6 = Very Common
        TrashSpawnRate = 4,
        -- Only active when 'Advanced Spawn Control' is enabled. Controls how often broken glass spawns. Default = Normal
        -- 1 = None
        -- 2 = Very Rare
        -- 3 = Rare
        -- 4 = Normal
        -- 5 = Common
        -- 6 = Very Common
        GlassSpawnRate = 4,
    },
    ConditionalSpeech = {
        SpeechCanAttractZombies = true,
        ShowOnlyAudibleSpeech = false,
        -- Disable phrases by writing out their IDs, separated by commas. Example: Bleeding,Sick,Hungry
        DisablePhrases = "",
    },
    BagUpgradePlus = {
        -- Controls how often zombies carry upgraded bags. 0 = Never, 100 = Always. Default: 10 (Rare) Min: 0 Max: 100 Default: 10
        UpgradedBagSpawnChance = 10,
    },
    BetterSafehouse = {
        -- Allows players to toggle a blue ground overlay showing their safehouse area.
        EnableSafehouseViewer = true,
        -- Allows inviting players even if they already own or belong to another safehouse.
        EnhancedInvites = true,
        -- Maximum number of safehouses a player can join with Enhanced invites ON. 0 = unlimited. Min: 0 Max: 20 Default: 0
        MaxJoinedSafehouses = 0,
        -- When a player enables respawn in one safehouse, Better Safehouse removes that player from the respawn list of all other safehouses.
        SingleRespawnSafehouseEnabled = true,
        -- Allows admins to add any player to a safehouse via the UI, without restrictions.
        AdminsFreeAddToSafehouse = true,
        -- Allows admins to remove/release a safehouse without changing its owner first.
        AdminsCanReleaseAnySafehouse = false,
        -- Enables custom claim BY ITEM. Incompatible with 'Custom claim anywhere (no item)'. Enable only one mode.
        CustomClaimEnabled = false,
        -- Only works when item-based custom claims are enabled and 'Custom claim anywhere (no item)' is disabled. Adds the CUSTOM option using the size defined in Sandbox and requires the 'customsafehouse' item.
        CustomClaimItemCustomSafehouse = false,
        -- Allows custom claim WITHOUT an item anywhere. Choose a single preset, 'Custom (sandbox)', or 'All' to unlock 15x15, 30x30, 60x60 and Custom. Incompatible with item mode (enable only one). Default = Disabled
        -- 1 = Disabled
        -- 2 = 15x15
        -- 3 = 30x30
        -- 4 = 60x60
        -- 5 = Custom Safehouse (sandbox)
        -- 6 = All (15x15 + 30x30 + 60x60 + Custom)
        CustomClaimFreeAnywhere = 1,
        -- Used when 'Custom Safehouse (sandbox)' is selected in free mode, and for the CUSTOM option in item mode (if enabled). Min: 3 Max: 200 Default: 31
        CustomSafehouseSize = 31,
        -- If enabled, blocks claiming inside existing safehouses, on roads/streets (tiles starting with 'blends_street') and nearby (distance set below).
        CustomClaimRestrictLocations = false,
        -- Used only when location restriction is enabled. Blocks claims within this many tiles of roads/streets and existing safehouses. Min: 0 Max: 200 Default: 10
        CustomClaimRestrictDistance = 10,
        -- Only works when the PhunZones 2 mod is active. If PhunZones 2 is not loaded, this option has no effect whether enabled or disabled.
        PhunZones2NoSafehouseBlock = true,
        -- If disabled, the 'Claim Safehouse' option will be blocked for all players. Use Custom Claim instead.
        VanillaSafehouseEnabled = true,
        -- Maximum building area (W*H tiles) allowed for vanilla safehouse claim. 0 = no limit. Min: 0 Max: 10000 Default: 0
        VanillaSafehouseAreaLimit = 0,
        -- Minimum building area required for vanilla safehouse claim. 0 = no minimum. Min: 0 Max: 10000 Default: 0
        VanillaSafehouseAreaMinimum = 0,
        -- Minutes a player must wait before claiming a new vanilla safehouse. 0 = no cooldown. Min: 0 Max: 43200 Default: 0
        VanillaSafehouseClaimCooldownMinutes = 0,
        -- Enables or disables the Better Safehouse expansion module.
        ExpansionEnabled = true,
        -- Roles that can freely expand and shrink. Comma-separated, example: Apoiador,VIP. The user role is ignored here.
        ExpansionAllowedRoleNames = "\"Apoiador\"",
        -- How many tiles each supporter/role click changes. Does not affect user. Min: 1 Max: 50 Default: 5
        ExpansionRoleStepTiles = 5,
        -- Extra-tile limit above the original safehouse for supporter/roles. Min: 0 Max: 20000 Default: 600
        ExpansionRoleMaxExtraTilesFromOriginal = 600,
        -- Enables the independent user system. It does not depend on allowed roles.
        ExpansionUserBorderExpansionEnabled = false,
        -- How many tiles user can push outward on each border from the original safehouse. Example: 1 turns 10x10 into 12x12. Min: 0 Max: 200 Default: 1
        ExpansionUserMaxBorderTilesFromOriginal = 1,
        -- When enabled, any expansion over configured road tiles is blocked.
        ExpansionBlockRoadTiles = false,
        -- Comma-separated road floor sprites. Only used when Block roads is enabled.
        ExpansionBlockedRoadTileNames = "\"blends_street_01_85",
    },
    OCRainWash = {
        -- Time required for downpour to fully clean a vehicle. Default is 1 hour. Min: 0.50 Max: 2.00 Default: 1.00
        DownpourCleanHours = 1.0,
        -- Time required for heavy rain to fully clean a vehicle. Default is 3 hours. Min: 1.50 Max: 6.00 Default: 3.00
        HeavyRainCleanHours = 3.0,
        -- Time required for moderate rain to fully clean a vehicle. Default is 6 hours. Min: 3.00 Max: 12.00 Default: 6.00
        ModerateRainCleanHours = 6.0,
        -- Time required for light drizzle to fully clean a vehicle. Default is 12 hours. Min: 6.00 Max: 24.00 Default: 12.00
        DrizzleCleanHours = 12.0,
    },
    DGMC_Bolt_Cutters = {
        -- whether the lock on garage doors can be cut open
        Allow_Garage_Doors = true,
        -- whether the lock on fence gates can be cut open
        Allow_Fence_Gates = true,
        -- whether bolt cutters can be used to destroy fence sections
        Allow_Fences = true,
        -- the percentage chance to drop a resource when destroying a fence section, 0 to disable Min: 0 Max: 100 Default: 0
        Fence_Wire_Chance = 0,
        -- whether the lock on security shutters over doors and windows can be cut open, the shutters will be destroyed
        Allow_Shutters = false,
        -- a character must have at least this level of strength to perform easy actions, like cutting thin wire fences Min: 0 Max: 10 Default: 3
        Easy_Strength_Req = 3,
        -- a character must have at least this level of strength to perform moderate actions, like cutting locks Min: 0 Max: 10 Default: 5
        Medium_Strength_Req = 5,
        -- a character must have at least this level of strength to perform challenging actions, like cutting thick fences Min: 0 Max: 10 Default: 7
        Hard_Strength_Req = 7,
        -- how many seconds it will take, before strength is factored in Min: 0 Max: 60 Default: 22
        Base_Duration = 22,
        -- how much muscle strain will be applied, before strength is factored in Min: 0.00 Max: 40.00 Default: 4.00
        Base_Muscle_Strain = 4.0,
        Debug_Logging = false,
    },
    JeevesJournals = {
        -- Default percentage of XP recovered when reading a journal. Per-category overrides below take priority when not set to -1. Min: 0 Max: 100 Default: 100
        RecoveryPercentage = 100,
        -- If enabled, recipes learned during gameplay will be stored in the journal and recoverable on read.
        RecoverRecipes = true,
        -- Recovery %% for passive skills (Fitness, Strength). Set -1 to use default. Set 0 to disable. Min: -1 Max: 100 Default: 0
        RecoverPassiveSkills = 0,
        -- Recovery %% for melee combat skills. Set -1 to use default. Min: -1 Max: 100 Default: -1
        RecoverCombatSkills = -1,
        -- Recovery %% for firearm skills. Set -1 to use default. Min: -1 Max: 100 Default: -1
        RecoverFirearmSkills = -1,
        -- Recovery %% for crafting skills. Set -1 to use default. Min: -1 Max: 100 Default: -1
        RecoverCraftingSkills = -1,
        -- Recovery %% for survivalist skills. Set -1 to use default. Min: -1 Max: 100 Default: -1
        RecoverSurvivalistSkills = -1,
        -- Recovery %% for farming skills. Set -1 to use default. Min: -1 Max: 100 Default: -1
        RecoverFarmingSkills = -1,
        -- Multiplier for how fast writing and reading progresses. Higher = faster. Min: 0.10 Max: 100.00 Default: 1.00
        TranscribeSpeed = 1.0,
        -- If enabled, each journal can only be read once per player. The XP is consumed on read.
        OneTimeUse = false,
        -- Override the journal crafting recipe inputs. Leave blank for default (Notebook + Glue + 3 Leather Strips + Thread).
        CraftRecipe = "",
        -- If enabled, XP gained from radio and TV will NOT be recorded in journals.
        DeductRadioTVXP = false,
        -- If enabled, map locations revealed by fliers and brochures will be stored in the journal and restored on read.
        RecoverMapKnowledge = true,
    },
    JeevesPC = {
        -- Allow arcade game floppy disks (Breakout, Pong, Snake, etc.) to spawn in loot.
        EnableGameDisks = true,
        -- Allow skill training floppy disks to spawn in loot.
        EnableTrainingDisks = true,
        -- Enable Aiming training disks.
        Skill_Aiming = true,
        -- Enable Reloading training disks.
        Skill_Reloading = true,
        -- Enable Axe training disks.
        Skill_Axe = true,
        -- Enable Long Blade training disks.
        Skill_LongBlade = true,
        -- Enable Long Blunt training disks.
        Skill_LongBlunt = true,
        -- Enable Maintenance training disks.
        Skill_Maintenance = true,
        -- Enable Short Blade training disks.
        Skill_ShortBlade = true,
        -- Enable Short Blunt training disks.
        Skill_ShortBlunt = true,
        -- Enable Spear training disks.
        Skill_Spear = true,
        -- Enable Blacksmithing training disks.
        Skill_Blacksmithing = true,
        -- Enable Carpentry training disks.
        Skill_Carpentry = true,
        -- Enable Carving training disks.
        Skill_Carving = true,
        -- Enable Cooking training disks.
        Skill_Cooking = true,
        -- Enable Electrical training disks.
        Skill_Electrical = true,
        -- Enable Glassmaking training disks.
        Skill_Glassmaking = true,
        -- Enable Knapping training disks.
        Skill_Knapping = true,
        -- Enable Masonry training disks.
        Skill_Masonry = true,
        -- Enable Mechanics training disks.
        Skill_Mechanics = true,
        -- Enable Pottery training disks.
        Skill_Pottery = true,
        -- Enable Tailoring training disks.
        Skill_Tailoring = true,
        -- Enable Welding training disks.
        Skill_Welding = true,
        -- Enable Agriculture training disks.
        Skill_Agriculture = true,
        -- Enable Animal Care training disks.
        Skill_AnimalCare = true,
        -- Enable Butchering training disks.
        Skill_Butchering = true,
        -- Enable First Aid training disks.
        Skill_FirstAid = true,
        -- Enable Fishing training disks.
        Skill_Fishing = true,
        -- Enable Foraging training disks.
        Skill_Foraging = true,
        -- Enable Tracking training disks.
        Skill_Tracking = true,
        -- Enable Trapping training disks.
        Skill_Trapping = true,
        -- Loot spawn weight for arcade game floppy disks. Higher = more common. Default: 0.5 Min: 0.00 Max: 20.00 Default: 0.50
        GameDiskWeight = 0.5,
        -- Loot spawn weight for skill training floppy disks. Higher = more common. Default: 0.3 Min: 0.00 Max: 20.00 Default: 0.30
        TrainingDiskWeight = 0.3,
        -- Total XP pool available from each Beginner (Tier I) training disk. Default: 75 Min: 0 Max: 10000 Default: 75
        XP_Beginner = 75,
        -- Total XP pool available from each Intermediate (Tier II) training disk. Default: 150 Min: 0 Max: 10000 Default: 150
        XP_Intermediate = 150,
        -- Total XP pool available from each Advanced (Tier III) training disk. Default: 300 Min: 0 Max: 10000 Default: 300
        XP_Advanced = 300,
        -- Training disks stop granting XP once the player reaches this skill level. 0 = no limit. Default: 5 Min: 0 Max: 10 Default: 5
        MaxSkillLevel = 5,
        -- How much boredom decreases every 5 seconds while playing arcade games. 0 = disabled. Default: 5 Min: 0 Max: 50 Default: 5
        BoredomReduction = 5,
        -- Multiplier for happiness gained at score milestones while playing arcade games. 0 = disabled. Default: 1.0 Min: 0.00 Max: 5.00 Default: 1.00
        HappinessMultiplier = 1.0,
        -- Extra lesson XP percentage for Stage 2 (Color) PCs. Default: 10 Min: 0 Max: 100 Default: 10
        Stage2XPBonus = 10,
        -- Extra lesson XP percentage for Stage 3 (Enhanced) PCs. Default: 20 Min: 0 Max: 100 Default: 20
        Stage3XPBonus = 20,
        -- Allow PC components (video cards, RAM, soldering irons) to spawn in loot.
        EnableComponentLoot = true,
        -- Multiplier for PC component loot spawn weights. Higher = more common. Default: 1.0 Min: 0.00 Max: 20.00 Default: 1.00
        ComponentLootWeight = 1.0,
        -- Allow corrupted, damaged, and encrypted data disks to spawn in the world and be recovered at computers.
        EnableDataDisks = true,
        -- Multiplier for data disk spawn rates in loot tables. 1.0 = default, 0.5 = half, 2.0 = double. Min: 0.00 Max: 5.00 Default: 1.00
        DataDiskSpawnChance = 1.0,
        -- Multiplier for XP recovered from data disks. 1.0 = default. Min: 0.00 Max: 5.00 Default: 1.00
        DataDiskXPMultiplier = 1.0,
        -- Data disks can teach recipes on recovery.
        DataDiskRecipeEnabled = true,
        -- Data disks can grant positive character traits on recovery.
        DataDiskTraitEnabled = true,
        -- Data disks can contain viruses that disable the computer until repaired.
        DataDiskVirusEnabled = true,
        -- How many real minutes a computer is disabled after a virus infection. Min: 1 Max: 480 Default: 30
        DataDiskVirusDowntime = 30,
        -- Data disks can inflict negative character traits on recovery.
        DataDiskNegTraitEnabled = true,
        -- Multiplier for the base virus chance on data disks. 1.0 = default. Min: 0.00 Max: 3.00 Default: 1.00
        DataDiskVirusChanceMult = 1.0,
        -- Multiplier for the chance of receiving a negative trait from data disks. Min: 0.00 Max: 3.00 Default: 1.00
        DataDiskNegTraitChanceMult = 1.0,
        -- Multiplier for data disk drops from zombie corpses. 1.0 = default. Min: 0.00 Max: 10.00 Default: 1.00
        ZombieDataDiskDropMult = 1.0,
        -- Allow players to record their skills onto blank floppy disks and recover them after death.
        EnablePersonalDisks = true,
        -- Percentage of recorded XP that can be recovered from personal data disks. 100 = full recovery. Min: 0 Max: 100 Default: 100
        PersonalDiskRecoveryPct = 100,
        -- Personal data disks also record and recover known recipes.
        PersonalDiskRecoverRecipes = true,
        -- Override recovery percentage for passive/physical skills. 0 = disabled by default. Min: -1 Max: 100 Default: 0
        PersonalDiskPassiveSkills = 0,
        -- Override recovery percentage for melee combat skills. -1 = use global setting. Min: -1 Max: 100 Default: -1
        PersonalDiskCombatSkills = -1,
        -- Override recovery percentage for firearm skills (Aiming, Reloading). -1 = use global setting. Min: -1 Max: 100 Default: -1
        PersonalDiskFirearmSkills = -1,
        -- Override recovery percentage for crafting skills. -1 = use global setting. Min: -1 Max: 100 Default: -1
        PersonalDiskCraftingSkills = -1,
        -- Override recovery percentage for survivalist skills (First Aid, Fishing, Foraging, Trapping, Tracking). -1 = use global setting. Min: -1 Max: 100 Default: -1
        PersonalDiskSurvivalistSkills = -1,
        -- Override recovery percentage for farming and animal care skills. -1 = use global setting. Min: -1 Max: 100 Default: -1
        PersonalDiskFarmingSkills = -1,
        -- If enabled, each personal data disk can only be loaded once per character.
        PersonalDiskOneTimeUse = false,
        -- Subtract XP earned from radio/TV skill tapes before recording to personal disks.
        PersonalDiskDeductRadioTVXP = false,
        -- Enable the Personal Digital Assistant feature. Disabling hides PDA items and context menu options.
        EnablePDA = true,
        -- Real-time minutes a full PDA battery lasts while the UI is open in idle mode. Default: 120 Min: 10 Max: 1440 Default: 120
        PDABatteryLife = 120,
        -- Enable PDA hacking of vanilla PCs and security doors.
        EnableHacking = true,
        -- Maximum hack attempts allowed on each vanilla PC before it is exhausted. Shared across all players. Default: 3 Min: 1 Max: 10 Default: 3
        PDAHackMaxAttempts = 3,
        -- In-game days before exhausted hack attempts reset on a vanilla PC. Default: 5 Min: 1 Max: 30 Default: 5
        PDAHackResetDays = 5,
        -- Base chance of a successful hack before skill and profession modifiers. Default: 25 Min: 5 Max: 75 Default: 25
        PDAHackSuccessChance = 25,
        -- Radius in tiles that PDA sounds attract nearby zombies. 0 = no attraction. Default: 15 Min: 0 Max: 50 Default: 15
        PDAZombieRadius = 15,
        -- Chance that a failed security door hack triggers a zombie-attracting alarm. Default: 50 Min: 0 Max: 100 Default: 50
        HackAlarmChance = 50,
        -- Radius in tiles that a door hack alarm attracts zombies. Default: 30 Min: 5 Max: 100 Default: 30
        HackAlarmRadius = 30,
        -- Allow players to craft and use the Scanner peripheral to digitize skill books onto Skill Library Disks.
        EnableBookScanner = true,
        -- Multiplier for book scanning duration. Lower values = faster scans. Default: 1.0 Min: 0.10 Max: 5.00 Default: 1.00
        ScannerSpeedMult = 1.0,
        -- Multiplier for reading time when studying a Skill Library Disk. Lower values = faster reading. Default: 1.0 Min: 0.10 Max: 5.00 Default: 1.00
        DiskReadSpeedMult = 1.0,
        -- Percentage of the book's XP multiplier applied when reading from a library disk. 100 = identical to reading the physical book. Default: 100 Min: 0 Max: 300 Default: 100
        DiskReadMultiplierPct = 100,
        -- Time multiplier when reading a Skill Library Disk on a PDA vs a PC. 1.0 = same speed, 2.0 = twice as long. Default: 1.5 Min: 1.00 Max: 5.00 Default: 1.50
        PDAReadTimePenalty = 1.5,
        -- Electrical skill level required to craft the Scanner. Default: 4 Min: 0 Max: 10 Default: 4
        ScannerCraftSkillReq = 4,
        -- Whether scanning a book awards a small amount of Electrical XP to the scanning player.
        ScanAwardsXP = true,
    },
    JeevesClaims = {
        -- Maximum number of safehouses a single player can own. (1-5) Min: 1 Max: 5 Default: 3
        MaxSafehouseClaims = 3,
        -- Maximum number of vehicles a single player can claim. (0-10) Set to 0 to disable vehicle claiming entirely. Min: 0 Max: 10 Default: 3
        MaxVehicleClaims = 3,
        -- Safehouses are automatically released after this many real days of owner inactivity. Set to 0 to disable. Min: 0 Max: 365 Default: 0
        SafehouseExpirationDays = 0,
        -- Claimed vehicles are automatically released after this many real days without owner interaction. Set to 0 to disable. Min: 0 Max: 365 Default: 14
        VehicleExpirationDays = 14,
        -- Semicolon-separated list of padding values players can choose when claiming a safehouse. Example: 0;2;5;10 gives four options. Values are tile counts added around each side of the building footprint. Set to just 0 for no padding.
        ClaimPaddingOptions = "0;2;4;6;8;10",
        -- Prevents claiming buildings within this many tiles of a player spawn point. Set to 0 to disable spawn protection. (0-200) Min: 0 Max: 200 Default: 50
        ProtectSpawnRadius = 50,
        -- Building must contain a living room to be considered residential. Only applies when SafehouseAllowNonResidential is false.
        ResidentialRequireLivingroom = true,
        -- Building must contain a kitchen to be considered residential. Only applies when SafehouseAllowNonResidential is false.
        ResidentialRequireKitchen = true,
        -- Building must contain a bedroom to be considered residential. Only applies when SafehouseAllowNonResidential is false.
        ResidentialRequireBedroom = true,
        -- Building must contain a bathroom to be considered residential. Only applies when SafehouseAllowNonResidential is false.
        ResidentialRequireBathroom = false,
        -- 1 = Must contain ALL checked room types. 2 = Must contain AT LEAST ONE checked room type. Min: 1 Max: 2 Default: 1
        ResidentialMatchMode = 1,
        -- When enabled, small garage and shed buildings (1-2 rooms) can be claimed if a residential building is nearby. Only applies when SafehouseAllowNonResidential is false.
        GarageProximityEnabled = true,
        -- When SafehouseAllowNonResidential is false, small buildings (like garages) that fail the room type check can still be claimed if a residential building is within this many tiles. Set to 0 to disable. (0-30) Min: 0 Max: 30 Default: 15
        GarageProximity = 15,
        -- Allow players to claim a predefined grid area for custom-built structures that PZ doesn't recognize as buildings. Claims cannot overlap existing buildings, roads, or other claims.
        CustomClaimEnabled = true,
        -- Available grid sizes for custom land claims, comma-separated. (e.g. 10,20,30,40)
        CustomClaimSizes = "10",
        -- When enabled, claiming a building locks all doors and gives the player 2 safehouse keys. Players can lock/unlock doors from either side via context menu.
        SafehouseKeysEnabled = true,
        -- Allow players to craft vehicle keys from the right-click context menu. Requires tools (hacksaw, file set) and a steel bar quarter.
        VehicleKeyCraftEnabled = true,
        -- Minimum Mechanics skill level required to craft a vehicle key. (0-10) Min: 0 Max: 10 Default: 5
        VehicleKeyCraftMechanics = 5,
        -- Minimum Electrical skill level required to craft a vehicle key. (0-10) Min: 0 Max: 10 Default: 2
        VehicleKeyCraftElectrical = 2,
        -- When enabled, claiming a trailer automatically gives the player a key for it. No skill or materials required.
        TrailerAutoKey = true,
        -- Number of in-game days a player must wait between claiming safehouses. Set to -1 to use the vanilla SafehouseDaySurvivedToClaim setting. Set to 0 for no cooldown. Min: -1 Max: 30 Default: -1
        ReclaimCooldownDays = -1,
        -- Admins, moderators, and GMs can claim safehouses without waiting for the reclaim cooldown.
        AdminBypassCooldown = true,
        -- When enabled, the target player must accept an in-game prompt before being added to a safehouse claim. The target must be online; the invite expires after 60 seconds. Admins always bypass this check and add members instantly.
        RequireAddMemberConsent = false,
        -- When enabled, players cannot claim safehouses inside zones tagged with the 'nosafehouse' property by the Phun Zones mod. Has no effect if Phun Zones is not installed. Lets server admins paint no-claim regions onto the map.
        RespectPhunZones = true,
    },
    PhunMart = {
        -- The probability that a zombie will drop coins upon death. Min: 0 Max: 100 Default: 30
        ChanceToDropChange = 30,
        -- The minimum number of cents a zombie can drop upon death. Min: 5 Max: 1000 Default: 5
        MinCoinsToDrop = 5,
        -- The maximum number of cents a zombie can drop upon death. Min: 10 Max: 1000 Default: 75
        MaxCoinsToDrop = 75,
        -- If enabled, players will drop their wallet upon death
        DropOnDeath = true,
        -- If enabled, only the owner of a wallet can pick it up.
        OnlyPickupOwn = true,
        -- If enabled, players can drop currency from their wallet as a pickupable item. Intentional drops are always pickupable by any player, regardless of the wallet pickup setting.
        AllowWalletDrop = true,
        -- The percentage of money that is returned to the player on death. 0 means no money is returned, 100 means all money is returned. Min: 1 Max: 100 Default: 100
        ReturnRate = 100,
        -- The chance that a vanilla vending machine will get converted to a random PhunMart machine. Set to 0 to disable Min: 0 Max: 100 Default: 80
        ChanceToConvert = 80,
        -- The minimum distance between similarly grouped machines Min: 0 Max: 10000 Default: 200
        DefaultDistance = 200,
        -- Maximum cents a player can carry (9999 = $99.99). At cap, coins left on the ground will not be consumed. Min: 0 Max: 999999 Default: 9999
        ChangeCapCents = 9999,
        -- Maximum number of special tokens a player can carry. Min: 0 Max: 9999 Default: 60
        TokenCap = 60,
        -- Show the change (coin) currency pool in the shop UI and wallet tab. Disabling hides it from players but does not delete balances.
        EnableChangePool = true,
        -- Show the token currency pool in the shop UI and wallet tab. Disabling hides it from players but does not delete balances.
        EnableTokenPool = true,
        -- The default number of hours between restocking a shop. 0 would mean that (by default) the shops are only ever stocked once Min: 0 Max: 9999999 Default: 72
        DefaultHoursToRestock = 72,
        -- The default number of hours between changing the shop to a different one. 0 means shops will default to never changing Min: 0 Max: 9999999 Default: 0
        DefaultNumOfHoursToReRoll = 0,
        -- This the number of items a shop will stock by default Min: 0 Max: 9999999 Default: 5
        DefaultNumOfItemsWhenRestocking = 5,
        -- Maximum number of items allowed in a sticky pool before a warning is logged. Sticky pools always show all their items in a shop. Keep this low to avoid cluttered shops. Min: 1 Max: 999 Default: 10
        MaxStickyItems = 10,
        -- Adds more verbose logging for debugging purposes. Only use if you know what you're doing.
        Debug = false,
        -- If set, only players whose role name matches this value (case-insensitive) can open the editor. Leave empty to allow all players with access to debug/admin menu (or always allow in singleplayer).
        EditorRole = "",
    },
    PhunServer = {
        -- Allow players to see who is online by typing /players into chat Default = Allow all
        -- 1 = Disable
        -- 2 = Allow admin
        -- 3 = Allow all
        PlayersCommand = 3,
        -- Include the list of players that have been online in the last 24 hours
        PlayersOffline24 = true,
        -- When ticked, allows admins or mods to set players hours survived using the format /sethours playername x. Note that player must be online. Playername is optional, if omitted it targets self
        SetHours = true,
        -- When ticked, allows players to view hours survived using the format /hours. Admins or mods can use /hours username (though the player needs to be online)
        GetHours = true,
        -- When ticked, we will refresh your settings with those found in your Sandbox_Vars.lua file. This is to workaround a bug in the current build where your settings get cached and subsequent changes ignored.
        RefreshSettingsOnStartup = true,
        -- Tick this to get more verbose debug info in your logs
        Debug = false,
        -- Announce when players join
        WelcomeAnnounce = true,
        -- If there is a value specified, PhunServer will use this text instead of the default welcome. Use %1$s as a placeholder for the players name. eg Welcome to the server %1$s
        WelcomeAnnounceText = "",
        -- Announce when players leave
        GoodbyeAnnouncements = true,
        -- If there is a value specified, PhunServer will use this text instead of the default goodbye. Use %1$s as a placeholder for the players name. eg Goodbye %1$s
        GoodbyeAnnounceText = "",
        -- Highlight known usernames in chat
        ColorUsernames = true,
        -- The RGB values to use instead of the default 255,255,255 leave blank for default
        ColorUsernameText = "",
        -- Replace [image=music] clutter in text with a little cute music note
        ReplaceMusic = true,
        -- Replace radio prefix with symbol to declutter chat
        ReplaceRadio = true,
        -- When ticked, will poll Steam for updates to your servers mods and insigate a reboot if any are found. Untick to disable
        EnableModWatch = true,
        -- Number of minutes between checking for changes to workshop Min: 1 Max: 100 Default: 5
        WorkshopPollingIntervalMinutes = 5,
        -- Default number of mins to give players notice of restart Min: 1 Max: 100 Default: 5
        RestartDelayMinutes = 5,
        -- A semi comma separated string of seconds between notification to clients
        NotificationCountdown = "300;120;60;30;10;9;8;7;6;5;3;2;1",
        -- Play a chime when notifying user of impending restart
        NotificationChime = true,
        -- Number of seconds after the final save to wait before quitting server Min: 1 Max: 100 Default: 15
        QuitDelaySeconds = 15,
        -- Show markers of player positions on map. Requires client restart. If you want this feature in B42+, you should disabled this and set MapRemotePlayerVisibility to 1 in your server ini Default = Disable
        -- 1 = Disable
        -- 2 = All
        -- 3 = Faction
        PlayersOnMap = 1,
        -- Show player positions on mini map. Requires client restart. If you want this feature in B42+, you should disable this and set MapRemotePlayerVisibility to 1 in your server ini Default = Disable
        -- 1 = Disable
        -- 2 = All
        -- 3 = Faction
        PlayersOnMiniMap = 1,
        -- Frequency in which to scan online players. 1000 = every second and should be a decent default Min: 0 Max: 10000 Default: 1500
        PlayersUpdateMs = 1500,
        -- When ticked, the below options will change the speed of your day and/or night cycles. Untick to disable these changes
        EnableDayNightChange = true,
        -- The speed at which night passes Default = 1 Hour
        -- 1 = 15 Minutes
        -- 2 = 30 Minutes
        -- 3 = 1 Hour
        -- 4 = 1 Hour, 30 Minutes
        -- 5 = 2 Hours
        -- 6 = 3 Hours
        -- 7 = 4 Hours
        -- 8 = 5 Hours
        -- 9 = 6 Hours
        -- 10 = 7 Hours
        -- 11 = 8 Hours
        -- 12 = 9 Hours
        -- 13 = 10 Hours
        -- 14 = 11 Hours
        -- 15 = 12 Hours
        -- 16 = 13 Hours
        -- 17 = 14 Hours
        -- 18 = 15 Hours
        -- 19 = 16 Hours
        -- 20 = 17 Hours
        -- 21 = 18 Hours
        -- 22 = 19 Hours
        -- 23 = 20 Hours
        -- 24 = 21 Hours
        -- 25 = 22 Hours
        -- 26 = 23 Hours
        NightSpeed = 3,
        -- +/- hours from dusk in which to trigger Night Speed Min: 0 Max: 24 Default: 0
        NightOffset = 0,
        -- The speed at which daytime passes Default = 1 Hour
        -- 1 = 15 Minutes
        -- 2 = 30 Minutes
        -- 3 = 1 Hour
        -- 4 = 1 Hour, 30 Minutes
        -- 5 = 2 Hours
        -- 6 = 3 Hours
        -- 7 = 4 Hours
        -- 8 = 5 Hours
        -- 9 = 6 Hours
        -- 10 = 7 Hours
        -- 11 = 8 Hours
        -- 12 = 9 Hours
        -- 13 = 10 Hours
        -- 14 = 11 Hours
        -- 15 = 12 Hours
        -- 16 = 13 Hours
        -- 17 = 14 Hours
        -- 18 = 15 Hours
        -- 19 = 16 Hours
        -- 20 = 17 Hours
        -- 21 = 18 Hours
        -- 22 = 19 Hours
        -- 23 = 20 Hours
        -- 24 = 21 Hours
        -- 25 = 22 Hours
        -- 26 = 23 Hours
        DaySpeed = 3,
        -- +/- hours from dawn in which to trigger Day Speed Min: 0 Max: 24 Default: 0
        DayOffset = 0,
        -- Untick to disable map wipe checks
        EnableWipeMap = true,
        -- Turn to false to skip erasure of the main map, even if the key changes
        WipeMap = true,
        -- Turn this off to skip erasure of symbols even if the key changes
        WipeSymbols = true,
        -- Wipes the map whenever the players character dies and they create a new one. A bit hardcore if you ask me, but you didn't did you?
        WipePerCharacter = false,
        -- Changing this value (as long as it isn't empty) will cause players to rewipe map on next login. A good rule of thumb here is to enter the version/season number. If a player comes back to the server and the season has changed... pop... there goes their map!
        WipeKey = "",
    },
    PhunSprinters = {
        -- This option governs when sprinters will run. ** = low performance impact, *** = med-high performance impact depending on population Default = Dusk till dawn
        -- 1 = Dusk till dawn
        -- 2 = Always
        -- 3 = When its too dark outside **
        -- 4 = When its too dark around them ***
        Mode = 1,
        -- If sprinter is running, light over your darkness level (eg a flashlight) can force them to walk (until its too dark again). Note that this is basically included in the tile based mode above
        SlowInLight = false,
        -- Percentage chance of a zed being a sprinter. If you use PhunZones, this is the fallback risk level when no other value is specified by a zone (or its parent). Examples: 0 = no chance. 50 = 50%% chance and 100 = always Min: 0 Max: 100 Default: 1
        DefaultRisk = 1,
        -- The number of hours (across all characters) until risk level is fully applied. For example, if this value is 240 (10 game days) then on the fifth day of play (regardless of how many times they have died), the effective risk that a player is reduced by 50%. Leave blank or 0 to ignore Min: 0 Max: 10000 Default: 0
        HoursDiscount = 0,
        -- All sprinters appear as Skeletons. CURRENTLY DISABLED AS BUG IN VANILLA CAN CAUSE A CLIENT CRASH WHEN AIMING AT A SKELETON
        Skeletons = true,
        -- Dress the sprinters up around the holidays (only works with certain additional mods active and installed)
        Decorate = true,
        -- Adjust risk on nights with a new moon by this value. eg 50 would cut the risk by 50%% while 200 would be 200%% (double the risk). Leave blank or 0 for no adjustment. Min: 0 Max: 1000 Default: 50
        MoonPhaseMultiplierNew = 50,
        -- Adjust risk on nights with a crescent moon by this value. eg 50 would cut the risk by 50%% while 200 would be 200%% (double the risk). Leave blank or 0 for no adjustment. Min: 0 Max: 1000 Default: 75
        MoonPhaseMultiplierCrescent = 75,
        -- Adjust risk on nights with a first quarter moon by this value. eg 50 would cut the risk by 50%% while 200 would be 200%% (double the risk). Leave blank or 0 for no adjustment. Min: 0 Max: 1000 Default: 90
        MoonPhaseMultiplierQuarter = 90,
        -- Adjust risk on nights with a gibbous moon by this value. eg 50 would cut the risk by 50%% while 200 would be 200%% (double the risk). Leave blank or 0 for no adjustment. Min: 0 Max: 1000 Default: 100
        MoonPhaseMultiplierGibbous = 100,
        -- Adjust risk on nights with a full moon by this value. eg 50 would cut the risk by 50%% while 200 would be 200%% (double the risk). Leave blank or 0 for no adjustment. Min: 0 Max: 1000 Default: 200
        MoonPhaseMultiplierFull = 200,
        -- Always display the UI component in the upper right screen. Requires restart
        Elements = true,
        -- If Always Show UI is disabled, tick this so that Military Issued sensor will appear in loot. Wearing these will show the UI. Requires restart. If you do not want any UI, disable this and the Always Show UI option
        AddToLoot = false,
        -- Default = Horizontal
        -- 1 = Vertical
        -- 2 = Horizontal
        layout = 2,
        -- Print verbosely (useful when diagnosing issues). Requires restart
        Debug = false,
        -- Adjusted light level where all sprinters will run Min: 0 Max: 100 Default: 74
        DarknessLevel = 74,
        -- The minimum distance of player to zed must be to process the chance of being a sprinter (this is to prevent sudden popins) Min: 1 Max: 100 Default: 14
        MinDistance2 = 14,
        -- The maximum distance of player to zed must be to process the chance of being a sprinter (this is to improve performance trying to process zeds that are too far away) Min: 1 Max: 100 Default: 35
        MaxDistance2 = 35,
        -- The max number of zeds to update per tick Min: 1 Max: 1000 Default: 20
        MaxQueue = 20,
        -- Volume of sprinter screech. 0 to disable Min: 0 Max: 100 Default: 10
        Volume = 10,
        -- Volume of the sound that notifies players that sprinters are no longer running (eg day) or that they have now started to run (eg night or bad weather). Set to 0 to disable Min: 0 Max: 100 Default: 15
        SprintingChangeNotificationVolume = 15,
    },
    PhunCure = {
        -- The chance out of 100 of a cure carrying zed appearing. eg 10 = 10%%, 5.5 = 5.5%%
        DefDropRate = ".1",
        -- The chance out of 100 that the sprinter is packing a cure. eg 10 = 10%%, 5.5 = 5.5%. Only applies if PhunSprinters is installed and rate differs from default
        DefSprinterDropRate = ".1",
        -- The chance (out of 100) that the cure will already be rotten which can further increase rarity. Note that if you disabled rotting below (eg Days to Rot = 0) then this value will have no affect. 0 means they will always be fresh, 50 means that half of the cures found will be unusable Min: 0 Max: 100 Default: 0
        ExpiredChance = 0,
        -- Number of days the cure is good for without keeping in fridge or freezer. Set to 0 or a crazy high number to disable (default is 4 days). Note this value only applies after a restart and only to newly created items Min: 0 Max: 10000 Default: 4
        DaysRotten = 4,
        -- Number of days that the cure is considered fresh. Currently has no benefit. Default is 1 day. Note that changing this value only applies after a restart and to newly created items Min: 0 Max: 10000 Default: 1
        DaysFresh = 1,
        -- Injecting a valid cure will remove the knox virus
        CureInfection = true,
        -- Injecting a valid cure will remove any infected wound (eg instead of using anti biotics). This is different to the knox virus
        CureWound = true,
        -- Injecting a valid cure will heal body part bite
        CureBite = true,
        -- Injecting a valid cure will heal any scratch
        CureScratch = true,
        -- Get verbose on it
        Debug = false,
    },
    LingeringVoices = {
        RespondToSound = true,
        CustomLines = true,
        -- Min: 0 Max: 604800 Default: 5
        LowerLineLimit = 5,
        -- Min: 0 Max: 604800 Default: 86400
        UpperLineLimit = 86400,
        -- Min: 0 Max: 1000 Default: 1
        StaggerSpeakChance = 1,
    },
    ThumpingAttractsZombies = {
        -- Min: 1 Max: 50 Default: 8
        BaseRange = 8,
        -- Min: 0.10 Max: 10.00 Default: 2.00
        ScalePerZombie = 2.0,
        -- Min: 0.10 Max: 2.00 Default: 0.80
        Exponent = 0.8,
        -- Min: 5 Max: 100 Default: 30
        MaxRange = 30,
    },
    PlayablePool = {
        -- Boredom reduced after a player takes a valid pool shot or minigame turn. Min: 0 Max: 100 Default: 18
        BoredomReliefPerTurn = 18,
        -- Maximum tile distance before players are too far away to use or keep the pool table window open. Min: 3 Max: 30 Default: 8
        MaxPlayDistance = 8,
        -- Allows debug/admin players to add the local Debug Bot for solo testing.
        AllowAdminSoloPractice = true,
        -- Allows a third player to watch an occupied table without joining the game.
        AllowSpectators = true,
        -- Shows darts, card games, chess, and checkers. These games are still in active development and may not work.
        EnableBetaMinigames = false,
        -- Pool sessions older than this are cleaned up automatically if abandoned. Min: 1 Max: 120 Default: 20
        AbandonedSessionMinutes = 20,
        -- Optional stress reduction after a valid pool shot or minigame turn. Leave at 0 to disable. Min: 0 Max: 100 Default: 0
        StressReliefPerTurn = 0,
        -- Optional unhappiness reduction after a valid pool shot or minigame turn. Leave at 0 to disable. Min: 0 Max: 100 Default: 0
        UnhappinessReliefPerTurn = 0,
    },
}