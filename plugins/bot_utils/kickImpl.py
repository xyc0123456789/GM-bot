# -*- coding: utf-8 -*-
import asyncio

from GetPathUtil import getTheBot


class KickReq:
    groupId = 111
    toKickIds = []
    message = "needed to call kick function"
    black = False
    kickSuccessIds = []
    kickFailIds = []
    countTop = 5
    delay = 0

    def __init__(self, group_id=0, toKickIds=[]):
        self.groupId=group_id
        self.toKickIds=toKickIds

    def __str__(self):
        add_str = "" if len(self.toKickIds)==0 else "\nKick todo: " + str(self.toKickIds)
        return (f"result:{self.message}\ntotal: {len(self.kickSuccessIds + self.kickFailIds)}\n"
                f"success: {len(self.kickSuccessIds)}, fail: {len(self.kickFailIds)}{add_str}")





async def botKick(group_id, user_id, black=False):
    bot = getTheBot()
    oneData = await bot.call_api("set_group_kick", group_id=group_id, user_id=user_id, reject_add_request=black)
    # print(user_id)


async def kick(kReq: KickReq):
    # print("delay", kReq.delay, len(kReq.toKickIds) == 0)
    if kReq.delay > 0:
        await asyncio.sleep(kReq.delay)
    error = None
    if kReq.groupId == 0:
        error = "group not found"
    if len(kReq.toKickIds) == 0:
        error = "kick finished"
    if error:
        kReq.message = error
        return error
    toRemove = []
    count = 0
    for id in kReq.toKickIds:
        try:
            count += 1
            await botKick(kReq.groupId, id, kReq.black)
            kReq.kickSuccessIds.append(id)
        except Exception as e:
            import traceback
            traceback.print_exception(e)
            kReq.kickFailIds.append(id)
        finally:
            toRemove.append(id)
        await asyncio.sleep(0.5)
        if 0 < kReq.countTop <= count:
            break
    for i in toRemove:
        kReq.toKickIds.remove(i)

    if len(kReq.toKickIds) == 0:
        kReq.delay = 0
        ans = await kick(kReq)
        return ans
    else:
        kReq.delay = 5
        ans = await kick(kReq)
        return ans


async def main():
    ans = await kick(kReq)
    print(ans)
    print(kReq)


if __name__ == '__main__':
    kReq = KickReq(group_id=11)
    for i in range(10):
        kReq.toKickIds.append(i)
    print(kReq)
    ll = asyncio.get_event_loop()
    ll.create_task(main())
    ll.run_forever()
