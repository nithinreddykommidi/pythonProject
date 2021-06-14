
# To know robot version
robot --version

# To run particular test case and Test cases 
    robot -t Testcase:1 TEST_SUITE.robot
    robot -t Testcase:1 -t "Test Case 3" TEST_SUITE.robot

# paasing values to variable through command line =>
    robot -v ONE:10 -v TWO:34 TEST_SUITE.robot

# validate the test data
    robot --dryrun TEST_SUITE.robot

# TO run a test case based on tag
    robot -i test2 TEST_SUITE.robot

# TO run all test cases except given tag
    robot -e test2 TEST_SUITE.robot

# Change logs path ==> 
    robot -d C:\ON-LINE\COURSES\2_ROBOT\Logs TEST_SUITE.robot
    robot -d LOGS TEST_SUITE.robot
                'OR'
    robot --outputdir LOGS TEST_SUITE.robot


