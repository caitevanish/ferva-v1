import React from 'react';
import { useState } from 'react';
// import CoursesTable from '../../components/CoursesTable/CoursesTable';
import CoursesTable from '../../components/CoursesTable/CoursesTable';
import Modal from 'react-modal';
import BarChart from '../../components/Chart/BarChart';

import useAuth from '../../hooks/useAuth';
import AddCourseForm from '../../components/Forms/Courses/AddCourseForm';
import { Button } from '@mui/material';
import { useNavigate } from 'react-router-dom';

const CoursesMainPage = (props) => {
  const { user, courses, rqstRld } = props;
  const [, token] = useAuth();
  // const [courses, setCourses] = useState([]);
  // const [courseDetails, setCourseDetails] = useState([]);
  const [modalIsOpen, setModalIsOpen] = useState(false);

  function getDatesList(courses) {
    let datesList = [];
    let dateData = courses.map((course) => course.purchase_date);
    console.log(dateData);
    return;
  }

  // useEffect(() => {
  //   fetchChart();
  // }, [courses]);

  //-----------To-Do:

  return (
    <div className='container-fluid'>
      <div className='row'>
        <h1>Courses Main Page</h1>
      </div>
      <div className='row'>
        <div className='col-md-7'>
          {/* <h2>My Courses</h2> */}
          <div className='feature-5'>
         
            <Button
              color='secondary'
              variant='contained'
              onClick={() => setModalIsOpen(true)}
            >
              Add a Course
            </Button>

            <CoursesTable courses={courses} token={token} />
          </div>
        </div>
        <div className='col-md-4'>
          <h2>Online Investments</h2>
          <div className='feature-6a'>
            <BarChart />
          </div>
        </div>
      </div>

      <Modal isOpen={modalIsOpen}>
        <AddCourseForm
          user={user}
          setModalIsOpen={setModalIsOpen}
          rqstRld={rqstRld}
        />
      </Modal>
      {/* <BarChart courses={courses} getDatesList={getDatesList} /> */}
    </div>
  );
};

export default CoursesMainPage;

//Past Code saved @ _scratch-temp > scratch-CoursesMain.js
