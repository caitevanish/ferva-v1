import React, { useState } from 'react';
import { Stack } from '@mui/material';
import './AddNewButtons.css';
import AddProjectForm from '../../Forms/Projects/AddProjectForm';
import Modal from 'react-modal';

function AddProjectButton({ height, sx }) {
  const [modalIsOpen, setModalIsOpen] = useState(false);

  return (
    <div>
      <Stack direction='column' spacing={0} sx={sx}>
        <button type='button' onClick={() => setModalIsOpen(true)}>
          <img src='/images/add-project.png' height={height} />
        </button>
        <p>Project</p>
      </Stack>

      <Modal isOpen={modalIsOpen}>
        <AddProjectForm setModalIsOpen={setModalIsOpen} />
      </Modal>
    </div>
  );
}

export default AddProjectButton;
