import unittest

import core


class TestCore(unittest.TestCase):
    def test_01_no_duplicate_book(self):
        state = core.new_game()
        self.assertTrue(core.book(state, 1))
        self.assertFalse(core.book(state, 1))

    def test_02_room_capacity(self):
        state = core.new_game()
        core.check_in(state, 1)
        core.check_in(state, 2)
        result = core.check_in(state, 3)
        self.assertFalse(result)

    def test_03_fee_exact(self):
        state = core.new_game()
        self.assertEqual(core.fee(state, 1, 3), 2)

    def test_04_cancel_refunds_oil(self):
        state = core.new_game()
        state["oil"] = 40
        core.cancel(state, 1)
        self.assertEqual(state["oil"], 50)

    def test_05_no_assign_absent_therapist(self):
        state = core.new_game()
        core.book(state, 1)
        result = core.assign(state, 1, "T2")
        self.assertFalse(result)

    def test_06_care_fail_no_cost(self):
        state = core.new_game()
        core.book(state, 1)
        state["bookings"][1]["failed"] = True
        before = state["oil"]
        result = core.care(state, 1)
        self.assertFalse(result)
        self.assertEqual(state["oil"], before)

    def test_07_allergy_once(self):
        state = core.new_game()
        core.book(state, 1)
        core.allergy(state, 1)
        self.assertEqual(state["bookings"][1]["health"], 90)

    def test_08_load_preserves_booking_id(self):
        state = core.new_game()
        state["booking_id"] = 4
        loaded = core.load_state(core.save_state(state))
        self.assertEqual(loaded["booking_id"], 4)


if __name__ == "__main__":
    unittest.main()
