# remoteGuidanceDisruptFalloff
#
# Used by:
# Variations of module: Guidance Disruptor I (6 of 6)
type = "active", "projected"


def handler(fit, module, context):
    if "projected" in context:
        for srcAttr, tgtAttr in (
                ("aoeCloudSizeBonus", "aoeCloudSize"),
                ("aoeVelocityBonus", "aoeVelocity"),
                ("missileVelocityBonus", "maxVelocity"),
                ("explosionDelayBonus", "explosionDelay"),
        ):
            fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                            tgtAttr, module.getModifiedItemAttr(srcAttr),
                                            stackingPenalties=True, remoteResists=True)
