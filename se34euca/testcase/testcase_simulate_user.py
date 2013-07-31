from se34euca.testcase.testcase_base import *

class testcase_simulate_user(testcase_base):

    def simulate_user_case_00(self):
        sleep_time = 2
        wait_time = 120
        print "=== runTest: Simulate User Case 00 ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.base.test_ui_gotopage_dashboard()
        self.eucaUITester.image.test_ui_gotopage_images()
        self.eucaUITester.base.test_ui_gotopage_dashboard()
        self.eucaUITester.keypair.test_ui_generate_keypair()
        self.eucaUITester.base.test_ui_gotopage_dashboard()
        self.eucaUITester.security_group.test_ui_create_security_group()
        self.eucaUITester.base.test_ui_gotopage_dashboard()
        self.eucaUITester.volume.test_ui_create_volume()
        time.sleep(sleep_time)
        self.eucaUITester.base.test_ui_gotopage_dashboard()
        self.eucaUITester.instance.test_ui_launch_instance_basic()
        print "Test: Simulate User Case 00 - Sleep for " + str(wait_time) + " Sec"
        time.sleep(wait_time)
        self.eucaUITester.base.test_ui_view_page_get_dashboard_source()
        self.eucaUITester.base.test_ui_gotopage_dashboard()
        self.eucaUITester.instance.test_ui_terminate_instance_all()
        self.eucaUITester.base.test_ui_gotopage_dashboard()
        self.eucaUITester.volume.test_ui_delete_volume_all()
        time.sleep(sleep_time)
        self.eucaUITester.base.test_ui_gotopage_dashboard()
        self.eucaUITester.security_group.test_ui_delete_security_group_all()
        self.eucaUITester.base.test_ui_gotopage_dashboard()
        self.eucaUITester.keypair.test_ui_delete_keypair_all()
        self.eucaUITester.base.test_ui_view_page_get_dashboard_source()

    def simulate_user_case_00_in_loop(self):
        sleep_time = 2
        wait_time = 120
        count = 0
        print "=== runTest: Simulate User Case 00 in Loop ==="
        self.eucaUITester.base.test_ui_login()
        while True:
            count += 1
            print "### TRIAL " + str(count) + " ###"
            try:
                print "Test: Simulate User Case 00 in Loop"
                print
                self.eucaUITester.base.test_ui_gotopage_dashboard()
                self.eucaUITester.image.test_ui_gotopage_images()
                self.eucaUITester.base.test_ui_gotopage_dashboard()
                self.eucaUITester.keypair.test_ui_generate_keypair()
                self.eucaUITester.base.test_ui_gotopage_dashboard()
                self.eucaUITester.security_group.test_ui_create_security_group()
                self.eucaUITester.base.test_ui_gotopage_dashboard()
                self.eucaUITester.volume.test_ui_create_volume()
                time.sleep(sleep_time)
                self.eucaUITester.base.test_ui_gotopage_dashboard()
                self.eucaUITester.instance.test_ui_launch_instance_basic()
                print "Test: Simulate User Case 00 in Loop - Sleep for " + str(wait_time) + " Sec"
                time.sleep(wait_time)
                self.eucaUITester.base.test_ui_view_page_get_dashboard_source()
                self.eucaUITester.base.test_ui_gotopage_dashboard()
                self.eucaUITester.instance.test_ui_terminate_instance_all()
                self.eucaUITester.base.test_ui_gotopage_dashboard()
                self.eucaUITester.volume.test_ui_delete_volume_all()
                time.sleep(sleep_time)
                self.eucaUITester.base.test_ui_gotopage_dashboard()
                self.eucaUITester.security_group.test_ui_delete_security_group_all()
                self.eucaUITester.base.test_ui_gotopage_dashboard()
                self.eucaUITester.keypair.test_ui_delete_keypair_all()
                self.eucaUITester.base.test_ui_view_page_get_dashboard_source()
                time.sleep(sleep_time)
            except Exception as inst:
                print type(inst)     # the exception instance
                print "Test: Simulate User Case 00 in Loop - Catched Exception: Try to Log Back In"
                print
                self.eucaUITester.base.test_ui_gotopage_dashboard()
                self.eucaUITester.base.test_ui_logout()
                time.sleep(sleep_time)
                self.eucaUITester.base.test_ui_login()

if __name__ == "__main__":
    unittest.main()



